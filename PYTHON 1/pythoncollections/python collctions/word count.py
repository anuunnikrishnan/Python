word={}
data="hello hai hello how are you hello"
dat=data.split(" ")
for item in dat:
    if(item not in word):
        word.update({item:1})
    else:
        count=int(word[item])
        count+=1
        word[item]=count
print(word)

