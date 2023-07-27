# Las colas en una estructura de datos lineal que usa la tecnica FiFo First in First Ou
# Esta estructura es buena para cualquier servicio en el que lo primero que llegue a una cola sea lo primero en salir
# En la cola la insercion y borrado de datos ocurren en lados opuestos.
# Hay varios tipos de cola:
# - Cirular
# - (input/output) restricted
# - Double ended Queue
# - Priority Queue: Ascending/ Descending 
# Operaciones de una Cola:
# - Enqueue(a): Agrega a la cola el item a
# - Dequeue(): saca de la cola un item, es sacado en el mismo orden en que fueron introducidos
# - front(): Obten el item que esta enfrente la cola
# - rear(): Obent el iten que esta ultimo en la cola


# Implementando colas usando lista
# Es la menos optima para su uso ya que la insercion requiere O(n)
from collections import deque
from queue import Queue

class QueueLst:
    def __init__(self):
        self.cola = []

    def __str__(self):
        return  'Cola(<- {} <-)'.format(self.cola)
    
    def __repr__(self):
        return  'Cola({})'.format(self.cola)
    
    def is_empty(self):
        if len(self.cola) == 0:
            return True
        else:
            return False
        #return True if len(self.cola) == 0 else False
    
    def enqueue(self, value):
        return self.cola.append(value)
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError('The Qeque is Empty')
        else:
            return self.cola.pop(0)
        
    def front(self):
        if self.is_empty():
            raise ValueError('The Qeque is Empty')
        else:
            return self.cola[0]
    def rear(self):
        if self.is_empty():
            raise ValueError('The Qeque is Empty')
        else:        
            return self.cola[-1]


def queue_using_deque():
    # Python program to
    # demonstrate queue implementation
    # using collections.dequeue




    # Initializing a queue
    q = deque()
    
    # Adding elements to a queue
    q.append('a')
    q.append('b')
    q.append('c')
    
    print("Initial queue")
    print(q)
    
    # Removing elements from a queue
    print("\nElements dequeued from the queue")
    print(q.popleft())
    print(q.popleft())
    print(q.popleft())
    
    print("\nQueue after removing elements")
    print(q)

    # Uncommenting q.popleft()
    # will raise an IndexError
    # as queue is now empty

def queue_using_queue_module():
    # Python program to
    # demonstrate implementation of
    # queue using queue module
    
    
    
    # Initializing a queue
    q = Queue(maxsize = 3)
    
    # qsize() give the maxsize
    # of the Queue
    print(q.qsize())
    
    # Adding of element to queue
    q.put('a')
    q.put('b')
    q.put('c')
    
    # Return Boolean for Full
    # Queue
    print("\nFull: ", q.full())
    
    # Removing element from queue
    print("\nElements dequeued from the queue")
    print(q.get())
    print(q.get())
    print(q.get())
    
    # Return Boolean for Empty
    # Queue
    print("\nEmpty: ", q.empty())
    
    q.put(1)
    print("\nEmpty: ", q.empty())
    print("Full: ", q.full())
    
    # This would result into Infinite
    # Loop as the Queue is empty.
    print(q.get())


#queue_using_deque()
queue_using_queue_module()