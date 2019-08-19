f=open("filetxt")
print(f)
print(f.mode)

print(f.readline())
print(f.read())
print(f.read())
to print even numbers from file
for i in f:
    if int(i)%2==0:
        print(i)
    else:
        pass
f=open("mydata.txt",'w')
# f.write("hello")
f.write("hai")
# will overwrite hello with hai to avoid this we use append function 'a'
f=open("mydata.txt",'a')
f.write("hello")






































