

def binarysearch(lst,elem):
    lst.sort()
    low=0
    upp=len(lst)
    mid=(low+upp)//2
    flag=0
    while(low<upp):
        if(elem<lst[mid]):
            upp=mid-1
        elif(elem>lst[mid]):
            low=mid+1
        elif(elem==lst[mid]):
            flag+=1
            break
        mid=(low+upp)//2
    if(flag==1):
        print("element found")
    else:
        print("element not found")
lst=[]
lim=int(input("enter how many elements u want to add"))
for i in range(0,lim):
    val=int(input("enter value to insert into list"))
    lst.append(val)
elem=int(input("enter the element to search"))
binarysearch(lst,elem)
