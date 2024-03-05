class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next  

def add_to_front(self, data):
    new_head = node(data, self) 
    return new_head 
    
def print_list_recursive(head):
    if head is not None:
        print(head.data)
        print_list_recursive(head.next) 

def print_list_iterative(head):
    current = head 
    while current:
        print(current.data)
        current = current.next 

def remove_from_front(head): 
    if head is None: 
        return None 
    return head.next 
    
def add_to_end(head, data):
    if head is None:
        return node(data)
    current = head 
    while current.next:
        current = current.next 
    current.next = node(data)
    return head 
    
def remove_from_end(head): 
    if head is None or head.next is None:
        return None 
    current = head 
    while current.next.next:
        current = current.next 
    current.next = None 
    return head 

print("Recursive") 
head = node(1, node(2, node(3))) 
print_list_recursive(head) 

print("Iterative") 
head = node(1, node(2, node(3))) 
print_list_iterative(head) 

print("Add to front") 
head = node(1, node(2, node(3))) 
head = add_to_front(head, 0) 
print_list_iterative(head) 

print("Remove from front") 
head = node(1, node(2, node(3))) 
head = remove_from_front(head) 
print_list_iterative(head) 

print("Add to end") 
head = node(1, node(2, node(3))) 
head = add_to_end(head, 4)
print_list_iterative(head) 

print("Remove from end") 
head = node(1, node(2, node(3))) 
head = remove_from_end(head) 
print_list_iterative(head) 


    


