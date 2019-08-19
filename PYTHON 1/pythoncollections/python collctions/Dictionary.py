dict={'Name':'Zara','Age':7,'class':'First'}
print("dict['Name']:",dict['Name'])
print("dict['Age')]:",dict['Age'])
dict['Age']=8
print("dict['Age']:after updation"),dict['Age']
print(dict.keys())
print('Name'in dict)
for val in dict.keys():
    print(dict[val])
print(val)
