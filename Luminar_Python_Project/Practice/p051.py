num=int(input("Enter the total number of bottles:"))
flag=0
while flag!=1:
    print(f"There are {num} green bottles hanging on the wall, {num} green bottles hanging on the wall and if 1 green bottle should accidentally fall")
    rem=int(input("How many bottles will be hanging on the wall:"))
    if rem==(num-1):
        num=num-1
        if num==0:
            break
        print("There will be", num ,"bottles hanging on the wall")
    else:
        print("Try again")
print("There are no more green bottles hanging on the wall")