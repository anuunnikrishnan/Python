def remainder(n):
    rem=n%2
    return rem

num=int(input("enter the number"))
for i in range(1,num):
    print(remainder(i))
