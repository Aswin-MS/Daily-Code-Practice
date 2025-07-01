#Attendance

total_class=int(input("Enter the total number of classes held:"))
attended=int(input("Enter the total number of classes attended:"))

attendance=(attended/total_class)*100

print(f"Attendance percentage:{attendance}%")

if attendance<75:
    print("You are not allowed to sit in the exam")
else:
    print("You are allowed to sit in the exam")