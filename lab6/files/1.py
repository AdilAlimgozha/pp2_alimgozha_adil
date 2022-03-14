import os

def printDir(path, level):
    for x in os.listdir(path):
        print(level, x)
        if os.path.isdir(x):
            printDir(x, level + "---")

printDir(".", "---")
#done