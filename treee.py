
class BT_node: 
    def __init__(self, data=None, left=None, right=None): 
        self.data = data
        self.left = left
        self.right = right 

class BinaryTree: 
    def __init__(self): 
        self.root = None  

    def populate_tree(self): 
        self.root = self.populate_tree_recur()
    
    def populate_tree_recur(self): 
        value = input("Enter the value of the node: ")  
        if value == "": 
            return None 
        new_node = BT_node 
        new_node.left = self.populate_tree_recur() 
        new_node.right = self.populate_tree_recur() 
        return new_node 
    


    def print_preorder(self): 
        self.print_preorder_recur(self.root) 

    def print_preorder_recur(self, node): 
        if node is None: 
            return 
        print(node.data, end=" ")
        self.print_preorder_recur(node.left) 
        self.print_preorder_recur(node.right) 

tree = BinaryTree() 
tree.populate_tree()   
tree.print_preorder()

