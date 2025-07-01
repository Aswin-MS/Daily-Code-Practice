#program

salary=int(input("Enter your salary:"))
total_year=int(input("Enter your year of service:"))

if total_year>5:
    bonus=salary*5/100
    print("Your bonus is",bonus)
else:
    print('You are ineligible for salary bonus!')