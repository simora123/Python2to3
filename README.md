Hello\

The following instructions are to assist in converting your python scripts from Python2 to Python3.\

The variables are set to directories associated with my work at York County Planning Commission but these directory paths can be changes at your local agency. You will need to adjust the folder variable (line 3) in the Convert_from_python2to3_Revised script provided.\

But here is the order you need to run these scripts and the batch file. I am sure there is a way to integrate all three steps into one python script or process but I just figured I would go about this way for now (updates/edits to this post coming....)\

Steps-\
1.\
Run python script Convert_from_python2to3_Revised.py - This will basically walk thru the directory to indicate and copy all .py files to selected folder destinated. This will organize all your python scripts into one centralized location. This will be essential for the following steps.\

2.\
After copying the Batch2 file in selected destination folder, run Batch2 batch file. This will run the out of the box 2to3.py script in the ArcGIS Pro install folder. This can be found under <Where you downloaded ArcGIS Pro>\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\Scripts. I copied the file to a local directory but you can change the C:\2to3\2to3.py variable in my batch file to wherever you like or revert to the install location. After you run, python2 script you have in the selected folder destination will be reverted to Python3 syntax.

3.\
Run YCPC_Convert_TexttoBatch.py. This script is pretty much hard coded so not much adjustments need changed in this script. Just make sure that this is also added to the selected folder destination as well. Script will look for python scripts in that folder, create a new text file, write the necessary lines of code in the text file to run as a batch file. The last step renames the text file to a .bat file.

Some things I still need to work on -\
1-\
Need to include if/else arguments. If file exists, then continue, else add file to directory.\
2-\
Some kind of if .bat file exists then don't try to rename to .bat.\

Any questions, please contact me at jsimora@ycpc.org or (717) 598-6530

