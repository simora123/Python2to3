import os, shutil

os.chdir(r"<Insert Directory Path>") ##Example r"O:\IS\Scripts"
DestinationFolder = "<Insert Destination Folder>" ##Example r"O:\IS\Backup_Scripts3"

for root, dirs, files in os.walk("."):
        for f in files:
                if f.endswith(".py"):
                    fpython = os.path.join("O:") + root.split(".")[-1] + "\\" + f
                    if os.path.exists(os.path.join(DestinationFolder,f)):
                        print("Exists in copy folder: {}".format(fpython))
                        pass
                    else:
                        shutil.copy2(fpython, DestinationFolder) # target filename is /dst/dir/file.ext
                        print ("Copied " + fpython)

print("Script Ends")
