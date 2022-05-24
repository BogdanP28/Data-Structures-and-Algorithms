class Range:
    """A class that mimic's the build-in range class"""
    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance
        Semantics is similar to build-in range class
        """
        if step == 0:
            raise ValueError('Step cannot be 0')
        
        if stop is None:                # special case of range(n)
            start, stop = 0, start      # should be treated as if range(0,n)
            
        # Calculate the effective length 
        self._length = max(0, (stop-start+step-1)//step)
        
        # need to know the start and step to support __getitem__
        self._start = start
        self._step = step
        
    def __len__(self):
        """Return the number of entries in the range"""
        return self._length
    
    def __getitem__(self,k):
        """Return entry at index k(using standard interpretation if negative)"""
        if k < 0:
            k += len(self)
        
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        
        return self._start + k * self._step
        
from abc import ABCMeta, abstractmethod
class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class"""
    
    @abstractmethod
    def __len__(self):
        """Return the length of the sequence"""
    @abstractmethod
    def __getitem__(self,j):
        """Return the element at index j of the sequence"""
        
    def __contains__(self,val):
        """Return True if val found in the sequence; False otherwise"""
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False
    
class Sequence2(Sequence):
    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1
        self._length = len(sequence)
    def __len__(self):
        """Return the number of entries in the range"""
        return self._length
    
    def __getitem__(self,k):
        """Return entry at index k(using standard interpretation if negative)"""
        if k < 0:
            k += len(self)
        
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        
        return self._start + k * self._step
        
aux = Sequence2([10])
print("here")

class SequenceIterator:
    """An iterator for any of Python's sequence types"""
    
    def __init__(self, sequence):
        """Create an iterator for the given sequence"""
        self._seq = sequence # keep a reference to the underlying data
        self._k = -1         # will increment to 0 on first call to next
        
    def __next__(self):
        """Return the next element, or else raise StopIteration error"""
        self._k += 1                     # advance to the next index
        if self._k < len(self._seq):
            return(self._seq[self._k])   # return the data element
        else:
            raise StopIteration()        # There are no more elements
        
    def __iter__(self):
        """By convention, an iterator must return iteself as an iterator"""
        return self
    
def main():
    aux = SequenceIterator([4,1,3])
    while aux:
        print(next(aux))
        
    print(next(aux))
    
def main2():
    aux = Range(10,step=2)
    for i in aux:
        print(i)
    print("here")
    
if __name__ == '__main__':
    main2()