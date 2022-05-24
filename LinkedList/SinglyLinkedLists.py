

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
            
    class LinkedListIterator:
        def __init__(self, head):
            self._current = head
            
        def __iter__(self):
            return self
        
        def __next__(self):
            if not self._current:
                raise StopIteration
            else:
                item = self._current._element
                self._current = self._current._next
                return item
            
    # ------------------------------- Stack methods -------------------------
    def __init__(self):
        """Create an empty stack"""
        self._head = None   # reference to the head node
        self._size = 0      # number of stack elements
        self._current = self._head
        
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
    
    def pop(self):
        """Remove and return the element from the top of the stack
        Raise empty exception if the stack is empty
        """
        if self.is_empty():
            raise Exception('Stack is empty')
        answer = self._head._element
        self._head = self._head._next        # Bypass the former top node
        self._size -= 1
        return answer
    
    def __iter__(self):
        return self.LinkedListIterator(self._head) 
    
    def __str__(self):
       
       return '->'.join(str(x) for x in self)




        
    
def main():
    lst = LinkedStack()
    for i in range(10):
        lst.push(i)
    print("Stack size: ", len(lst))
    print('Top', lst.top())
    print('Pop', lst.pop())
    print('Top', lst.top())
    print(lst)
    
if __name__ == '__main__':
    main()
    
    