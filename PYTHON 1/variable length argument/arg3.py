# key =i value =j
# data items to fetch value from dictionary
def person(**data):
    for i,j in data.items():
        print(i,j)
person(name='navin',age=24,city='mumbai')