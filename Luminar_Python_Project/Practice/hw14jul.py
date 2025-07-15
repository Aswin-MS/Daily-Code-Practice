def fib(num):
    temp = 0
    fibo = 1
    for i in range(0,num):
        if i==0:
            fibo=0
        elif i==1:
            fibo=1
        else:
            oldfib=fibo
            fibo += temp
            temp=oldfib
        print(fibo,",",end=' ')

num=int(input("Enter the number:"))
fib(num)