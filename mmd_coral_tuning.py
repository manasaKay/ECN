import os

lmds = ['0.3']
lmd_exts = ['0.33', '0.66', '1']
ignore = []

for lmd in lmds:
    for lmd_ext in lmd_exts:
        if (lmd, lmd_ext) in ignore:
            continue
        print(lmd, lmd_ext)
        os.system("python3 main.py -s duke -t market -mmd 1 --lmd %s --lmd_ext %s >log_mmd_d_m_%s,%s.txt 2>error.txt" % (lmd, lmd_ext, lmd, lmd_ext))
        os.system("python3 main.py -s market -t duke -mmd 1 --lmd %s --lmd_ext %s >log_mmd_m_d_%s,%s.txt 2>error.txt" % (lmd, lmd_ext, lmd, lmd_ext))
        os.system("python3 main.py -s duke -t market -coral 1 --lmd %s --lmd_ext %s >log_coral_d_m_%s,%s.txt 2>error.txt" % (lmd, lmd_ext, lmd, lmd_ext))
        os.system("python3 main.py -s market -t duke -coral 1 --lmd %s --lmd_ext %s >log_coral_m_d_%s,%s.txt 2>error.txt" % (lmd, lmd_ext, lmd, lmd_ext))
