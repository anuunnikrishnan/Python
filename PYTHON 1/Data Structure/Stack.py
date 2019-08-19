stack=[]
top=-1
def push(element):
    global top
    if((top+1)>=size):
        print("Stack is full")
    else:
        top+=1
        stack.insert(top,element)
        print("Element Inserted")
def pop(element):
    global top
    if(top<0):
        print("stack is empty")
    else:
        print("deleted element",stack[top])
        top=top-1
        print("element deleted")
def display(element):
    global top
    for i in range(0,top+1):
        print("Elements are",stack[i])
size=int(input("enter the size of the stack"))
con=0
while(con!=2):
    print("1.Push 2.POP 3.Display 4.Exit")
    ch = int(input("enter your choice"))
    if(ch==1):
        element=int(input("Enter the element"))
        push(element)
    elif (ch==2):
        pop(element)
    elif(ch==3):
        display(element)
    else:
        print("Invalid input")
    con=int(input("Do you want to continue 1.Yes 2.No"))

