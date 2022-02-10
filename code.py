import time
the = time.time() - (30 * 24 * 60 * 60)
import os
import shutil
import stat
path = input("enter the path of the folder you want Bin30 to get set to ")
ctime = os.stat(path).st_mtime
list_of_files = os.listdir(path)
for file in list_of_files:
    #name,ext = os.path.splitext(file)
    var = os.walk(path)
    #ext = ext[1:]  
    if ctime > the:
        files = os.path.join(path,file)
        os.chmod(files , stat.S_IWRITE)
        os.remove(files)

