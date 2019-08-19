class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
#         [none,none]
class Linked_list:
    def __init__(self):
        self.head=Node()
    def append(self,data):
        new_node=Node(data)
        # [10,none]
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node
    def length(self):
        cur=self.head
        total=0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total
    def display(self):
        elems=[]
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)
    def search(self,element):
        cur_node=self.head
        flag=0
        while(cur_node.next!=None):
            cur_node=cur_node.next
            if(element==cur_node.data):
                print("Element found")
                flag=1
                break
        if(flag==0):
            print("Element not found")
lst=Linked_list()
lst.append(10)
lst.append(20)
lst.append(30)
lst.display()
print("length is",lst.length())
element=int(input("Enter the element to search"))
lst.search(element)