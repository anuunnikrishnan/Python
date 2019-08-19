lst=["abc","cde","efgh","ijk"]
f=open("lstout.txt","a")
for item in lst:
    f.write(item+"\n")

    # to read value from file and store it in list
    # f=open("name.txt")
    # lst=[]
    # for i in f:
    #     lst.append(i)
    # print(lst)
# to avoid /n
    lst = []
    f = open("name.txt")
    for i in f:
        lst.append(i.rstrip("\n"))
    print(lst)
