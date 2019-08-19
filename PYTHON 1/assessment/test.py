n=int(input("Enter the number"))
if(n%2!=0):
    print("weird")
elif n%2==0 and(n in range(2,5)or(n>20)):
    print("not weird")
elif n%2==0 and (n in range(6,20)):
    print("weird")