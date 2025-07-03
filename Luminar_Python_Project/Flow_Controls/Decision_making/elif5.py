#calculate road tax of a bike
price=int(input("Enter the price of your bike:"))

if price>100000:
    tax= price*15/100
    print("Your road tax is", tax)
elif price>=50000:
    tax= price*10/100
    print("Your road tax is", tax)
else:
    tax = price * 5 / 100
    print("Your road tax is", tax)

"""
OR
We don't need to print all the statements in 
every block, we can only use one print statement
outside the decision making.
"""
