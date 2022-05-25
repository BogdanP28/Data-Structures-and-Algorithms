

class LinkedQueue:
    """FIFO queue implementation using a singly linked list"""
    
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node"""
        def __init__(self, element, next):
            self._element = element
            self._next = next
            
    class LinkedListIterator:
        """Iterator used to pass through queue"""
        def __init__(self, head):
            self._current = head
            
        def __iter__(self):
            return self
        
        def __next__(self):
            return self
            
        def __next__(self):
            if not self._current:
                raise StopIteration
            else:
                item = self._current._element
                self._current = self._current._next
                return item
            
    def __init__(self):
        """Create an empty queue"""
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        """Return(but not remove) the element at the front of the queue"""
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._head._element
    
    def last(self):
        """Return(but not remove) the element at the tail of the queue"""
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._tail._element
    
    def dequeue(self):
        """Remove and return the first element of the queue
        Raise Empty exception is queue is empty"""
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():              # Special case as queue is empty
            self._tail = None            # Removed head had been the tail
        return answer
    
    def enqueue(self, e):
        """Add an element to the back of the queue"""
        newest = self._Node(e, None)     # node will be new tail node
        if self.is_empty():
            self._head = newest          # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest              # Update reference to tail node
        self._size += 1     
        
    def __iter__(self):
        return self.LinkedListIterator(self._head)
    
    def __str__(self):
        return '->'.join(str(x) for x in self)
    
def main():
    queue = LinkedQueue()
    for i in range(10):
        queue.enqueue(i)
    
    print('Queue:', queue)
    print('First Element', queue.first())
    print('Dequeue', queue.dequeue())
    print('Queue:', queue)
    
    print('Last element: ', queue.last())


if __name__ == '__main__':
    main()
        