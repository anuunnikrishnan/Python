
# square function
# normal
# def square(n):
#     sqr=n*n
#     return sqr
#
# num=int(input("enter the number"))
# for i in range(1,num):
#     print(square(i))

# using lambda

# res=lambda no:no*no
# print(res(10))

# square function
# val=lambda num:num*num
# print(val(10))


# even or odd

# normal
# def isEven(num):
#     if(num%2==0):
#         return  True
#     else:
#         return False
# print(isEven(18))

# using lambda
# chkEven=lambda no:True if no%2==0 else False
# print(chkEven(5))

for i in (1,10):
    chkEven=lambda no:True if no%2==0 else False
    print(chkEven(i))
