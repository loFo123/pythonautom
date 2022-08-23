import os.path
import re
import subprocess
import sys
count = 0
pics = []
texts = []
videos = []
# os.mkdir("pics")
c =0;
for line in sys.stdin:
    if line.__contains__(".jpg") or line.__contains__(".png") or line.__contains__(".jpeg") :
        pics.append(line.strip())



print("---------pics--------")
print(pics)