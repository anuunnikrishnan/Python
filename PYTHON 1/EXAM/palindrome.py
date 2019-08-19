def palindrome(num):
    rev=0
    n=num
    while(n>0):
        r=n%10
        n = n//10
        rev=rev*10+r
    if(num==rev):
            print("number is palindrome")
    else:
            print("number is not palindrome")
num=int(input("enter the number"))
palindrome(num)
