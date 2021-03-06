import os

lmds = ['0', '0.3']
lmd_exts = ['0.33', '0.66', '1']
ignore = []

for lmd in lmds:
    for lmd_ext in lmd_exts:
        if (lmd, lmd_ext) in ignore:
            continue
        print(lmd, lmd_ext)
        os.system("python3 main.py -s duke -t market -cs cyclegan -mmd 1 --lmd %s --lmd_ext %s >log_mmd_d_m_%s,%s.txt 2>error.txt" % (lmd, lmd_ext, lmd, lmd_ext))
        os.system("python3 main.py -s market -t duke -cs cyclegan -mmd 1 --lmd %s --lmd_ext %s >log_mmd_m_d_%s,%s.txt 2>error.txt" % (lmd, lmd_ext, lmd, lmd_ext))
        os.system("python3 main.py -s duke -t market -cs cyclegan -coral 1 --lmd %s --lmd_ext %s >log_coral_d_m_%s,%s.txt 2>error.txt" % (lmd, lmd_ext, lmd, lmd_ext))
        os.system("python3 main.py -s market -t duke -cs cyclegan -coral 1 --lmd %s --lmd_ext %s >log_coral_m_d_%s,%s.txt 2>error.txt" % (lmd, lmd_ext, lmd, lmd_ext))

os.system("python3 main.py -s duke -t market -cs stargan -mmd 1 --lmd 0.3 --lmd_ext 0.33 >log_stargan_d_m_%s,%s.txt 2>error.txt" % (0.3, 0.33, 0.3, 0.33))
os.system("python3 main.py -s market -t duke -cs stargan -mmd 1 --lmd 0.3 --lmd_ext 0.33 >log_stargan_m_d_%s,%s.txt 2>error.txt" % (0.3, 0.33, 0.3, 0.33))
