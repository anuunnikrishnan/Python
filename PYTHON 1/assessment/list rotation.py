# given an input list[123456]after rotation it must be [456123]or[561234]
def rotate(lst,n):
    lst2=[]
    for i in range(len(lst)-n,len(lst)):
        lst2.append(lst[i])
    for i in range(0,len(lst)-n):
        lst2.append(lst[i])
    print("Result is",lst2)
lst=[1,2,3,4,5,6]
n=int(input("Enter the position"))
print("List is :  ",lst)
rotate(lst,n)


