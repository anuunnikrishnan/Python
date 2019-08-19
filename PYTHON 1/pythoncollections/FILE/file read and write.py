# read from one file and write to another file
fin=open("mydata.txt")
f=open("fileout.txt",'a')
for val in fin:
    f.write(val)

