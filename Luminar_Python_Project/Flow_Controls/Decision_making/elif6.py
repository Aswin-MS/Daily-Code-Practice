#Calculate Electricity bill

unit=int(input("Enter the unit of power consumed:"))

if unit<=100:
    cost=0
elif 101<=unit<=200:
    cost=(unit-100)*5

else:
    n_unit=unit-100
    cost=(100*5)+((n_unit-100)*10)

print(f'Charge for your electricity is Rs',cost)

"""
The amount above 200 will always have a fixed amount of 500
As first 100 is free of cost
and the second 100 unit (101-200) is at a cost of 500
Then the rest of the unit is multiplied by 10
eg:350 unit
    350-100=250 #the first 100 is free
    250-100=150 #now cost=500(100*5)
    150*10=1500 # rest 150 *10
    total cost = 500+1500=2000
"""