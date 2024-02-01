class ArrayList: 
    def __init__(self):
        self.capacity = 4 
        self.size = 0 
        self.arr = [0] self.capacity 

def append(array_list, value): 
    array_list.arr[array_list.size] = value 
    array_list.size += 1 

def print_array(array_list): 
    for i in range(array_list.size): 
        print(array_list.arr[i]) 

array_list = ArrayList() 
append(array_list, 1) 
append(array_list, 2) 
append(array_list, 3) 
append(array_list, 4) 

print_array(array_list)