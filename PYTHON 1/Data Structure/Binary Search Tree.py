class node:
    def __init__(self,value=None):
        self.value=value
        self.left_child=None
        self.right_child=None
class binary_search_tree:
    def __init__(self):
        self.root=None
    def insert(self,value):
        if self.root==None:
            self.root=node(value)
        # node(value) means invoking constructor ..to set value calling the class node
        else:
            self._insert(value,self.root)
    #     _insert is a private method as we have to use the function recursively from same class
    def _insert(self,value,cur_node):
        if value<cur_node.value:
            if cur_node.left_child==None:
                cur_node.left_child=node(value)
            else:
                self._insert(value,cur_node.left_child)
        elif value>cur_node.value:
            if cur_node.right_child==None:
                cur_node.right_child=node(value)
            else:
                self._insert(value,cur_node.right_child)
        else:
            print("value already in tree")
    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)
    def _print_tree(self,cur_node):
        if cur_node!=None:
            # print(str(cur_node.value))
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            # if we have to use preorder,postorder change the print stmt to first and last
            self._print_tree(cur_node.right_child)
            # print(str(cur_node.value))postorder
    def search(self,value):
        if self.root!=None:
            return self._search(value,self.root)
        else:
            return False
    def _search(self,value,cur_node):
        if value==cur_node.value:
            print("Element Found")
            return True
        elif value<cur_node.value and cur_node.left_child!=None:
            return self._search(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self._search(value,cur_node.right_child)
        else:
            print("Element not found")
            return False


btree=binary_search_tree()
btree.insert(25)
btree.insert(18)
btree.insert(28)
btree.insert(20)
btree.insert(30)
btree.insert(15)
btree.print_tree()
btree.search(30)

