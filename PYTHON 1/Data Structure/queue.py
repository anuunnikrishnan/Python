queue=[]
front=0
rear=-1
def add(element):
    global rear
    if(rear+1>=size):
        print("Queue is full")
    else:
        rear+=1
        queue.insert(rear,element)
        print("Element Inserted")

def delete():
            global front
            global rear
            if(front>rear):
                print("Queue is empty")
            else:
                print("deleted element", queue[front])
                front= front+1
                print("element deleted")
def display():
            global rear
            for i in range(front,rear+1):
                print("Elements are",queue[i])
size=int(input("enter the size of the queue"))
con=0
while(con!=2):
    print("1.Insert 2.Delete 3.Display 4.Exit")
    ch = int(input("enter your choice"))
    if(ch==1):
        element=int(input("Enter the element"))
        add(element)
    elif (ch==2):
        delete()
    elif(ch==3):
        display()
    else:
        print("Invalid input")
    con=int(input("Do you want to continue 1.Yes 2.No"))
