def sum1(list,element):
    low=0
    upp=len(list)
    while(low<upp):
        if(sum<upp):
            upper=upper-1
        else:
            lower=lower+1
        if(sum==(low+upp)):
            print("ordered pair of sum is",list[low],list[upp])
length=int(input("enter the length of the list"))
list=[]
list.sort()
for i in range(0,length):
    element=int(input("enter the element"))
    list.append(element)
print(list)
sum=int(input("enter the sum"))
sum1(list,element)


