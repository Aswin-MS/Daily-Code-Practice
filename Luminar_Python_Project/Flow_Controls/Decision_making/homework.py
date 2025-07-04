c_year=int(input("Enter the current year(YYYY):"))
c_month=int(input("Enter the current month(MM):"))
c_date=int(input("Enter the current date(DD):"))

b_year=int(input("Enter the birth year(YYYY):"))
b_month=int(input("Enter the birth month(MM):"))
b_date=int(input("Enter the birth date(DD):"))

print(f'You were born on {b_date}/{b_month}/{b_year}')
print(f'Today is {c_date}/{c_month}/{c_year}')
if (c_date>31)|(b_date>31) | (c_month>12)|(b_month>12):
    print("INVALID INPUTS")
    exit()
age=0
if b_year<c_year:
    if b_month<c_month:
        age=c_year-b_year
    elif b_month==c_month:
        if (b_date<c_date)|(b_date==c_date):
            age = c_year - b_year
        elif b_date>c_date:
            age=c_year-b_year-1
    else:
        age=c_year-b_year-1
elif b_year==c_year:
    age=0
else:
    age=''
    print("INVALID YEAR!")

if age!='':
    print("You are",age,"years old")