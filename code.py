import time
the = time.time() - 30*864000
import os
import shutil
path = input("enter the path of the folder you want Bin30 to get set to ")
list_of_files = os.listdir(path)
for file in list_of_files:
    name,ext = os.path.splitext(file)
    ext = ext[1:]
    if os.path.exists(path):    
        os.walk(path)
        os.path.join(path)
        ctime = os.stat(path).st_mtime
        if ctime > the:
            if ext == '':
                shutil.rmtree()
            else:
                os.remove(path)
    else:
        print("not found!!!!!!!!")

