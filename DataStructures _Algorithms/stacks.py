# Los stacks utilizan el metodo Last In / First Out or LIFO
# Los casos de uso de los stacks son para backtrace, Undo, etc.
# los metodos principales que se utilizan en stack son 
# push(i) pone un item en el stack
# pop() quita el ultimo elemento del stack
# otros metodos 
# empty(): Retorna si el stack esta vacio O(1)
# size(): Retorna el tamaño del stack O(1)
# top()/peek(): Retorna el indice del tope del stack
from collections import deque
from queue import LifoQueue

# implementation using list
# Are could be very slow with great amount of data, as list allocation are serialized, append coul take more than normal. 

class StackLst():
    def __init__(self, max_size=None):
        self.stack = []
        self.max_size = max_size
    def __str__(self):
        return 'stack {}\nStack currenz size: {}\nstack max size: {}'.format(self.stack, self.size(), self.max_size)
    def __repr__(self):
        return 'StackLst({}'.format(self.stack)
    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False
    def size(self):
        return len(self.stack)
    def push(self, item):
        if self.size() != self.max_size:
            self.stack.append(item)
        else:
            raise IndexError('The stack is full')
    def pop(self):
        if not self.is_empty():
            self.stack.pop()
        else:
            raise IndexError('The stack is empty')
    def top(self):
        if self.is_empty():
            raise IndexError('The stack is Empty')
        return self.stack[-1]


# Python program to demonstrate
# stack implementation using a linked list.
# node class

class Node:    
    def __init__(self, value):
        self.value = value  
        self.next = None


class Stack:

	# Initializing a stack.
	# Use a dummy node, which is
	# easier for handling edge cases.
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]    
    # Get the current size of the stack
    def getSize(self):
        return self.size    
    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0    
    # Get the top item of the stack
    def peek(self):    
        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value    
    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1    
    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value    


def using_stack_linked_list():
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")    
    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")



# using collections.deque
# is the fastes but not threat safe
def stack_using_deque():
    stack = deque()
 
    # append() function to push
    # element in the stack
    stack.append('a')
    stack.append('b')
    stack.append('c')
 
    print('Initial stack:')
    print(stack)
 
    # pop() function to pop
    # element from stack in
    # LIFO order
    print('\nElements popped from stack:')
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
 
    print('\nStack after elements are popped:')
    print(stack)
 
# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty


# Stack using LIFO Queue in queue.LifoQueue
# Slower than deque but threat safe

def using_lifoqueue():
    # Initializing a stack
    stack = LifoQueue(maxsize=3)
 
    # qsize() show the number of elements
    # in the stack
    print(stack.qsize())
 
    # put() function to push
    # element in the stack
    stack.put('a')
    stack.put('b')
    stack.put('c')
 
    print("Full: ", stack.full())
    print("Size: ", stack.qsize())
 
    # get() function to pop
    # element from stack in
    # LIFO order
    print('\nElements popped from the stack')
    print(stack.get())
    print(stack.get())
    print(stack.get())
    print("\nEmpty: ", stack.empty())

# Implementing stack using single linked list:
#

 
#stack_using_deque()
using_lifoqueue()    
using_stack_linked_list()