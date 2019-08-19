# mark=[10,20,30,40,10]
# for i in range(0):
#      if(i%2==0):
#          print(mark)
# print(mark)
# print(mark[0:2])
# mark[1]=25
# print(mark)
# list=[10,1,20,25,30,35,40]
# print(list)
# even=[]
# odd=[]
# for i in list:
    # print(i)
    # if(i%2==0):
    #     even.append(i)
    # else:
    #     odd.append(i)
# print(odd)
# print(even)
# print(len(odd))
# print(len(even))
# print(odd.count(35))
# print(max(odd))
# print(min(even))

length=int(input("enter the length of the list"))
list=[]
for i in range(0,length):
    element=int(input("enter the element"))
    list.append(element)
# print(list)
print("list before sorting",list)
list.sort()
print("list after sorting",list)
# print(list)

