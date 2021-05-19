import os
import sys
import subprocess

os.chdir("D:\\Leetcode");
string='''
#include<bits/stdc++.h>
using namespace std;
class Solution{
    public:

};
int main(){
    Solution s;
    auto ans=s.func();
    return 0;
}
'''
with open(sys.argv[1],"w") as f:
    f.write(string)
subprocess.run("code D:\\Leetcode",shell=True)
subprocess.run("code D:\\Leetcode\\"+sys.argv[1],shell=True)


