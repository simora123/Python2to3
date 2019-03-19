import os, shutil

folder = ["Python", "Expressions", "Misc", "pasda_update"]

os.chdir(r"O:\IS\Scripts")

for fold in folder:
    os.chdir(os.path.join(r"O:\IS\Scripts",fold))
    for root, dirs, files in os.walk("."):
        for f in files:
                if f.endswith(".py"):
                    fpython = os.path.join("O:\IS\Scripts",fold) + root.split(".")[-1] + "\\" + f
                    shutil.copy2(fpython, r'O:\IS\Backup_Scripts2') # target filename is /dst/dir/file.ext
                    print ("Copied " + fpython)

import glob, os
os.chdir(r"O:\IS\Scripts")
for file in glob.glob("*.py"):
    #print file
    fpython = "O:\IS\Scripts" + "\\" + file
    shutil.copy2(fpython, r'O:\IS\Backup_Scripts2') # target filename is /dst/dir/file.ext
    print ("Copied " + fpython)
