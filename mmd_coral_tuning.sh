lmds="0 0.3"
lmd_exts="0 0.33 0.66 1"
for lmd in $lmds
do
    for lmd_ext in $lmd_exts
    do
        echo $lmd, $lmd_ext
        python3 main.py -s duke -t market -mmd 1 --lmd $lmd --lmd_ext $lmd_ext >"log_mmd_$lmd,$lmd_ext.txt" 2>error.txt
        python3 main.py -s market -t duke -coral 1 --lmd $lmd --lmd_ext $lmd_ext >"log_coral_$lmd,$lmd_ext.txt" 2>error.txt
        rm logs/log.txt
    done
done