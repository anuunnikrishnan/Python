def vowels(str):
    set1=set()
    count=0
    set2={'a','e','i','o','u','A','E','I','O','U'}
    for i in str:
        if i in set2:
            count+=1
            set1.add(i)
        else:
            pass
    if count==0:
        print("No vowels present in the string")
    else:
        print("Number of vowels present in the string is :",count)
str=input("enter the string")
vowels(str)


