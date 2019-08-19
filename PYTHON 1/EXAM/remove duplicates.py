def remove(lst):

    lst2=[]
    for i in lst1:
        if i not in lst2:
            lst2.append(i)
    print(lst2)
lst1=[]
n=int(input("enter the number of elements"))
for i in range(0,n+1):
    el=int(input("enter the no. of elements"))
    lst1.append(el)
remove(lst1)
