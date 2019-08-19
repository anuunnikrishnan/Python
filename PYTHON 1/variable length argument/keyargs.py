# kwargs act as dictionary key,value pair...in place of kwargs data also possible
def person(name,**kwargs):
    print(name)
    print(kwargs)
person("navin",age=24,city='mumbai')