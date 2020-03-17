from __future__ import print_function, absolute_import
import time

import torch
from torch.autograd import Variable

from .evaluation_metrics import accuracy
from .utils.meters import AverageMeter
import copy
import numpy as np
import visdom
import os
import torch.nn.functional as F
from reid.loss.mmd import MmdLoss
from reid.loss.coral import CoralLoss

class Trainer(object):
    def __init__(self, model, model_inv, lmd=0.3, include_mmd=0, include_coral=0, lmd_ext=0):
        super(Trainer, self).__init__()
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = model
        self.model_inv = model_inv
        self.pid_criterion = torch.nn.CrossEntropyLoss().to(self.device)
        self.lmd = lmd
        self.include_mmd = include_mmd
        self.include_coral = include_coral
        self.lmd_ext = lmd_ext
        print(
            "lmd:", self.lmd,
            "lmd_ext:", self.lmd_ext,
            "include_mmd:", self.include_mmd,
            "include_coral:", self.include_coral,
        )
        self.mmd_criterion = MmdLoss()
        self.coral_criterion = CoralLoss

    def train(self, epoch, data_loader, target_train_loader, optimizer, print_freq=1):
        self.set_model_train()

        batch_time = AverageMeter()
        data_time = AverageMeter()
        losses = AverageMeter()
        precisions = AverageMeter()

        end = time.time()

        # Target iter
        target_iter = iter(target_train_loader)

        # Train
        for i, inputs in enumerate(data_loader):
            data_time.update(time.time() - end)

            # Source inputs
            inputs, pids = self._parse_data(inputs)

            # Target inputs
            try:
                inputs_target = next(target_iter)
            except:
                target_iter = iter(target_train_loader)
                inputs_target = next(target_iter)
            inputs_target, index_target = self._parse_tgt_data(inputs_target)

            # Source pid loss
            outputs_source, outputs_source_partial = self.model(inputs, 'src_feat')
            source_pid_loss = self.pid_criterion(outputs_source, pids)
            prec, = accuracy(outputs_source.data, pids.data)
            prec1 = prec[0]

            # Target invariance loss
            outputs_target = self.model(inputs_target, 'tgt_feat')
            loss_un = self.model_inv(outputs_target, index_target, epoch=epoch)

            # Mmd loss and Coral Loss
            if self.include_mmd:
                loss_mmd = self.mmd_criterion(outputs_source_partial, outputs_target)
                loss = (1 - self.lmd) * source_pid_loss + self.lmd * loss_un + self.lmd_ext * loss_mmd
            elif self.include_coral:
                loss_coral = self.coral_criterion(outputs_source_partial, outputs_target)
                loss = (1 - self.lmd) * source_pid_loss + self.lmd * loss_un + self.lmd_ext * loss_coral
            else:
                loss = (1 - self.lmd) * source_pid_loss + self.lmd * loss_un

            loss_print = {}
            loss_print['s_pid_loss'] = source_pid_loss.item()
            loss_print['t_un_loss'] = loss_un.item()

            losses.update(loss.item(), outputs_target.size(0))
            precisions.update(prec1, outputs_target.size(0))

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            batch_time.update(time.time() - end)
            end = time.time()

            if (i + 1) % print_freq == 0:
                log = "Epoch: [{}][{}/{}], Time {:.3f} ({:.3f}), Data {:.3f} ({:.3f}), Loss {:.3f} ({:.3f}), Prec {:.2%} ({:.2%})" \
                    .format(epoch, i + 1, len(data_loader),
                            batch_time.val, batch_time.avg,
                            data_time.val, data_time.avg,
                            losses.val, losses.avg,
                            precisions.val, precisions.avg)

                for tag, value in loss_print.items():
                    log += ", {}: {:.4f}".format(tag, value)
                print(log)

    def _parse_data(self, inputs):
        imgs, _, pids, _ = inputs
        inputs = imgs.to(self.device)
        pids = pids.to(self.device)
        return inputs, pids

    def _parse_tgt_data(self, inputs_target):
        inputs, _, _, index = inputs_target
        inputs = inputs.to(self.device)
        index = index.to(self.device)
        return inputs, index

    def set_model_train(self):
        self.model.train()

        # Fix first BN
        fixed_bns = []
        for idx, (name, module) in enumerate(self.model.module.named_modules()):
            if name.find("layer3") != -1:
                # assert len(fixed_bns) == 22
                break
            if name.find("bn") != -1:
                fixed_bns.append(name)
                module.eval()
