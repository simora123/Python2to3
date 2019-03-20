import glob, os

pylist = []
# Set Directory for Batch File Location
os.chdir(r"<Insert Working Directory>")##Example r"O:\IS\Backup_Scripts"
# For Loop - Searches files in Set Directory. Set to look for .py files(python)
for file in glob.glob("*.py"):
    print(file)
    pylist.append(file)

# Varify python files in pylist
print(pylist)
# Varify name of python file
print(__file__)

# Variable to propy file. This file is needed in order to run python3 in batch file environment
pyfile2 = "<Insert propy script location>" ##Example r"C:\Program Files (x86)\ArcGIS\Pro\bin\Python\Scripts\propy"

#For Loop- Loops thru pylist. Python files have been appended
for py in pylist:
    # Basically saying if the python code is called the name of this python file ignore. Else proceed
    if py != __file__.split("\\")[-1]:
        #Getting path of this python file
        pythonfile = os.getcwd()
        # Opening new text file
        f= open("{}.txt".format(py.split(".")[0]), "w+")
        # Write the follwing into the text file
        f.write("rem : /k is for interactive run, /c is for scheduled run and requires full UNC path\n\
    set mytime=%date:~10,4%-%date:~4,2%-%date:~7,2%_%time:~0,2%-%time:~3,2%\n\
    set mytime=%mytime: =%")
        f.write("""\n\ncmd /c "{}" {} > {}_%mytime%.txt""".format(pyfile2, os.path.join(pythonfile,py), os.path.join(pythonfile,py.split(".")[0])))
        # Close text file
        f.close()
        # Split name of python file
        base = os.path.splitext(py)[0]
        # Rename text file to .bat
        os.rename(py.split(".")[0] + ".txt", "Batch_" + base + ".bat")
