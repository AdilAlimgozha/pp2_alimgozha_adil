import os

print("exist:", os.access("lab6", os.F_OK))
print("read:", os.access("lab6", os.R_OK))
print("write:", os.access("lab6", os.W_OK))
print("execute:", os.access("lab6", os.X_OK))
#done