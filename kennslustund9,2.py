class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        self.top = Node(data, self.top)
        self.size += 1

    def pop(self):
        if self.top is None:
            raise IndexError("Poppa úr tómum stack")
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def get_size(self):
        return self.size

    def __str__(self):
        current = self.top
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return ' -> '.join(elements)

class Queue:
    def __init__(self):
        self.front = self.rear = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def pop(self):
        if self.front is None:
            raise IndexError("Pop from an empty queue")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return data

    def get_size(self):
        return self.size

    def __str__(self):
        current = self.front
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return ' -> '.join(elements)

print("Stack") 
s = Stack() 
s.push(1)
s.push(2)
s.push(3)
print(s)
print(s.pop())
print(s)
print(s.get_size())

print("Queue")
q = Queue()
q.push(1)
q.push(2)
q.push(3)
print(q)
print(q.pop())
print(q)

