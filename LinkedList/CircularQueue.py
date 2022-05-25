

class CircularQueue:
    """Queue implementation using circularly linked list for storage"""
    
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node"""
        def __init__(self, element, next):
            self._element = element
            self._next = next
            
    def __init__(self):
        """Create an empty queue."""
        self._tail = None       # will represent tail of queue
        self._size = 0          # number of queue elements
        
    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size
    
    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0
    
    