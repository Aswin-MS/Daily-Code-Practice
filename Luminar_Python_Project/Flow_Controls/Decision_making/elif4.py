mark1=int(input("Enter marks obtained for test1:"))
mark2=int(input("Enter marks obtained for test2:"))
mark3=int(input("Enter marks obtained for test3:"))
mark4=int(input("Enter marks obtained for test4:"))
t_mark=mark1+mark2+mark3+mark4
print("Total mark is:",t_mark)

if t_mark>=180:
    print("You have obtained A+ grade")
elif 160<=t_mark<=179:
    print("You have obtained A grade")
elif 140<=t_mark<=159:
    print("You have obtained B+ grade")
elif 120<=t_mark<=159:
    print("You have obtained B grade")
elif 100<=t_mark<=139:
    print("You have obtained C+ grade")
elif 80<=t_mark<=99:
    print("You have obtained C grade")
else:
    print("FAIL")

'''
#OR
if t_mark>=180:
    print("A+")
elif t_mark>=160:
    print("A")
elif t_mark>=140:
    print("B+")
elif t_mark>=120:
    print("B+")
elif t_mark>=100:
    print("C+")
elif t_mark>=80:
    print("C")
else:
    print("FAIL")
'''