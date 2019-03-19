import glob, os

pylist = []
os.chdir(r"O:\IS\Backup_Scripts")
for file in glob.glob("*.py"):
    print(file)
    pylist.append(file)

print(pylist)

print(__file__)

pyfile2 = r"C:\Program Files (x86)\ArcGIS\Pro\bin\Python\Scripts\propy"

for py in pylist:
    if py != __file__.split("\\")[-1]:
        pythonfile = os.getcwd()
        f= open("{}.txt".format(py.split(".")[0]), "w+")
        f.write("rem : /k is for interactive run, /c is for scheduled run and requires full UNC path\n\
    set mytime=%date:~10,4%-%date:~4,2%-%date:~7,2%_%time:~0,2%-%time:~3,2%\n\
    set mytime=%mytime: =%")
        f.write("""\n\ncmd /c "{}" {} > {}_%mytime%.txt""".format(pyfile2, os.path.join(pythonfile,py), os.path.join(pythonfile,py.split(".")[0])))
        f.close()
        base = os.path.splitext(py)[0]
        os.rename(py.split(".")[0] + ".txt", "Batch_" + base + ".bat")