def lcm(a,b):
    for i in range(1,a*b,1):
        if i%a==0 and i%b==0:
            print("LCM of given numbers is :",i)
            break
a=int(input("enter the first number"))
b=int(input("enter the second number"))
lcm(a,b)