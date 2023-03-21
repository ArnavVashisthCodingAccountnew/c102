import os
import shutil

from_dir = "C:/Users/arnav/Downloads"
to_dir = "C:/Users/arnav/arnav coding/c102project/Document_files"


list_of_files = os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    f,b = os.path.splitext(file)
    if(b == ""):
        continue
    elif b == ".pdf" or b == ".docx" or b == ".doc" or b == ".txt" or  b == ".pdf":
        path1 = from_dir + '/' + file
        path3 = to_dir + '/' + "Document_files"
        path2 = to_dir + '/' + "Document_files" + '/' + file 
        if os.path.exists(path2):
            print("Moving the file to the folder")
            shutil.move(path1, path2)
        else:
            os.makedirs(path2)  
            print("Moving the file to the folder")
            shutil.move(path1, path2) 


