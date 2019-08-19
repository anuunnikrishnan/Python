# global variable
name="luminar"
# local variable ph
# def disp(ph):
#     print(name)
#     print(ph)
# print(name)
# disp(9846226098)

# to change global variable in function
def disp():
    global name
    name="technolab"
    print("inside",name)
disp()
print("outside",name)