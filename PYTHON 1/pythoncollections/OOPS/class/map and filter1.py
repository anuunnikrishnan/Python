lst=["anu","sai","sanuja","hima"]
names=list(map(lambda str:str.upper(),lst))
print(names)

fname=list(filter(lambda x:x.startswith('s'),lst))
print(fname)