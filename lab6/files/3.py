import os
x = "C:\ПП1\code Python 2 semester\lab6"
if os.access(x, os.F_OK):
    print("direcroty:", os.path.dirname(x))
    print("name:", os.path.basename(x))
else:
    print("This path does not exist")
#done