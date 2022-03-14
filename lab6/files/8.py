import os

if os.path.exists("lab6/files/file_for_delete.txt"):
    os.remove("lab6/files/file_for_delete.txt")
else:
    print("file does not exist")
#done