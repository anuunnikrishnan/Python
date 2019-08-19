# filter using normal function
# list=[1,6,4,2,7,9]
# for i in list:
#     if i%2==0:
#         print(i)
#     else:
#         pass
# def isEven(num):
#     if(num%2==0):
#         return True
#     else:
#         return False
# lst=[10,20,21,23,25,28,30]
# evelist=list(filter(isEven,lst))
# print(evelist)

# filter using lambda function

lst=[10,20,21,23,25,28,30]
evelst=list(filter(lambda x:x%2==0,lst))
print(evelst)