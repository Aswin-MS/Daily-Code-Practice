num1=10
num2=20
print("Before swapping:")
print('number1 is ',num1)
print(f'number2 is ',num2)

num1=num1+num2
num2=num1-num2
num1=num1-num2
#num1,num2=num2,num1--> This also right
print('After swapping')
print('number1 is ',num1)
print(f'number2 is ',num2)