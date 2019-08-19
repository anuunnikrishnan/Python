# input names in fname,input phoneno in fphno and write these names and phoneno in fnp
# using file
# fname=open("name.txt")
# fphno=open("phonenumber.txt")
# fnp=open("name and phoneno.txt",'a')
# for val in fname:
#      fnp.write(val)
#      for val in fphno:
#          fnp.write(val)
#          break

# using list
fname=open("name.txt")
lst1=[]
for i in fname:
    lst1.append(i.rstrip("\n"))
fphno=open("phonenumber.txt")
lst2=[]
for i in fphno:
    lst2.append(i.rstrip("\n"))
# print(lst1)
# print(lst2)
fnp=open("name and phoneno.txt",'w')
for val in lst1:
    for v in lst2:
        fnp.write(val+" "+v+"\n")
        break



