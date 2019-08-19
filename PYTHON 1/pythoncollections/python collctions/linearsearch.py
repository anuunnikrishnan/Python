def linearsearch(lst,element):
    flg=0
    for i in lst:

        if(i==element):
            flg+=1
            break
        else:
            flg=0
    if(flg==0):
        return False
    else:
        return True
lst=[]
lim=int(input("enter how many elements u want to add"))
for i in range(0,lim):
    val=int(input("enter value to insert into list"))
    lst.append(val)
element=int(input("enter the element to search"))
print(linearsearch(lst,element))

