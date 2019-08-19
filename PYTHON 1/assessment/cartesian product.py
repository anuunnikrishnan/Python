# list1=[1,2,3]
# list2=[5,6,7]
#
# for i in list1:
#     for j in list2:
#         print(i,j)

# list comprehension
A=[1,2,3]
B=[4,5,6]
cartesianproduct=[(a,b)for a in A for b in B]
print(cartesianproduct)