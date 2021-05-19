import os
import sys
count=1
for filename in os.listdir():
    components=filename.split(".")
    if(filename!=sys.argv[0]):
        while(True):
            try:
                os.rename(filename,str(count)+"."+components[-1])
                break
            except Exception as e:
                count+=1