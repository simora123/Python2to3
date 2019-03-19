import os, shutil

# Predined folder that are at your organization. The following are folders that live under the os.chdir - r"O:\IS\Scripts"
folder = ["Python", "Expressions", "Misc", "pasda_update"]

# Changing directory path. This is the location that the os.walk will run
os.chdir(r"O:\IS\Scripts")

#For Loop - loops thru folder variable
for fold in folder:
    # Changes directory path
    os.chdir(os.path.join(r"O:\IS\Scripts",fold))
    # os.walk - will walk thru every file of the os.chdir. If .py extension copy to destination folder
    for root, dirs, files in os.walk("."):
        for f in files:
                if f.endswith(".py"):
                    # Location of python file under os.chdir
                    fpython = os.path.join("O:\IS\Scripts",fold) + root.split(".")[-1] + "\\" + f
                    # Copy python file under os.chdir to destination folder
                    shutil.copy2(fpython, r'O:\IS\Backup_Scripts2') # target filename is /dst/dir/file.ext
                    print ("Copied " + fpython)
                    
# Added step to get files under the O:\IS\Scripts directory
import glob, os
os.chdir(r"O:\IS\Scripts")
for file in glob.glob("*.py"):
    #print file
    fpython = "O:\IS\Scripts" + "\\" + file
    shutil.copy2(fpython, r'O:\IS\Backup_Scripts2') # target filename is /dst/dir/file.ext
    print ("Copied " + fpython)
