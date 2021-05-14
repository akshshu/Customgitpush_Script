from os import mkdir
import os
import sys
if(sys.argv[1]=="Easy"):
    path="D:\\Leetcode\\Leetcode\\Easy\\"+sys.argv[2]
    os.makedirs(path)
elif(sys.argv[1]=="Medium"):
    path="D:\\Leetcode\\Leetcode\\Medium\\"+sys.argv[2]
    os.makedirs(path)
desc=input("enter description\n")
file=open(path+"\\Readme.md","w")
file.write(desc)
file2=open("D:\\Leetcode\\"+sys.argv[3],"rb")
content=file2.read()
file3= open(path+"\\"+sys.argv[3],"wb")
file3.write(content)


file.close()
file2.close()
file3.close()
import subprocess
os.chdir("D:\\Leetcode\\Leetcode")
subprocess.check_output(["git","add", path])
    # to check if subprocess call has raised an error if yes Called process error is set to 1
if subprocess.CalledProcessError == 1:
    print("Error in adding files to git ")
    exit(1)
subprocess.check_output(["git","commit","-m", str(sys.argv[3])+" added"])
if subprocess.CalledProcessError == 1:
    print("Error in commiting")
    exit(1)
subprocess.check_output(["git","push", "origin","master"])
if subprocess.CalledProcessError == 1:
    print("Error in pushing to github")
    exit(1)





