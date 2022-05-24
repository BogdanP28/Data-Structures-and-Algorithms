

class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""
    #   ----------------------------- nested _Node class ---------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node"""
        __slots__ = '_element', '_next'     # streamline memory usage
        
        def __init__(self, element, next):
            """Initialize node's fields

            Args:
                element (_type_): reference to user's element
                next (function): reference to next node
            """
            self._element = element
            self._next = next
    # ------------------------------- Stack methods -------------------------
    def __init__(self):
        """Create an empty stack"""
        self._head = None   # reference to the head node
        self._size = 0      # number of stack elements
        
    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size
    
    def is_empty(self):
        """Return True if stack is empty"""
        return self._size == 0
    
    def push(self, element):
        """Add element e to the top of the stack"""
        self._head = self._Node(element, self._head)
        self._size += 1
        
    def top(self):
        """Return(but not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty"""
        
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._head._element
    
def main():
    lst = LinkedStack()
    for i in range(10):
        lst.push(i)
    print("Stack size: ", len(lst))
    print('Top', lst.top())
    
if __name__ == '__main__':
    main()
    
    