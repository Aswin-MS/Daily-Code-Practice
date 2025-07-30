"""
File Operations
------------------>
3 types:
1)read-----> r
2)write----> w
3)append---> a
#syntax:
var=open('argument1','argument2')
here, argument1=file path and argument 2= mode of operation
"""
#eg:
f=open('sample','r')
for i in f:
    print(i,end='')