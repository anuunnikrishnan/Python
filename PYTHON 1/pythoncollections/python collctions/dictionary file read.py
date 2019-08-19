dict={}
for x in f:
    lst=x.split(",")
    if lst[0] not in dict:
        dict.update({lst[0]:int(lst[1])}
    else:
        temp=dict[lst[0]]
        if(int(lst[1]>temp)):
            temp=lst[1]
            dict.update({lst[0]:int(lst[1])})
for i in dict:
    print(i,":",dict[i]))
