class Progression:
    """Iterator producing a generic progression.
    Default iterator produces the whole numbers 0, 1, 2..
    """
    
    def __init__(self, start=0):
        """Initialize current to the first value of the progression."""
        self._current = start
        self._tester = 9
        
    def _advance(self):
        """Update self._current to a new value.
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the end of a finite progression.
        """
        self._current += 1
        
    def __next__(self):
        """Return the next element, or else raise StopIteration error"""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current      # record current value to return
            self._advance()             # advance to prepare for next time
            return answer               # return the answer
        
    def __iter__(self):
        """By convention, an iterator must return itself as an interator"""
        return self
    
    def print_progression(self, n):
        """Print next n values of the progression"""
        print(' '.join(str(next(self)) for j in range(n)))
        
        
class ArithmeticProgression(Progression):       # inherit from Progression
    """Iterator producing an arithmetic progression"""
    
    def __init__(self, increment=1, start=0):
        """Create a new arithmetic progression

        Args:
            increment (int, optional): the fixed constant to add to each term. Defaults to 1.
            start (int, optional): the first term of the progression. Defaults to 0.
        """
        super().__init__(start)     # Initialize base class
        self._increment = increment
        
    def _advance(self):
        """Update current value by adding the fixed increment"""
        self._current += self._increment

class GeometricProgression(Progression):    # inherit form Progression
    """Iterator producing a geometric progression"""
    def __init__(self, base=2, start=1):
        """Create a new geometric progression

        Args:
            base (int, optional): the fixed constant to multiply to each term. Defaults to 2.
            start (int, optional): the first term of the progression. Defaults to 1.
        """
        super().__init__(start)
        self._base = base
        
    def _advance(self):
        """Update the current value by multiplying it base the base value"""
        self._current *= self._base
        
class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression"""
    
    def __init__(self, first=0, second=1):
        """Create a new fibonacci sequence

        Args:
            first (int, optional): the first term of the progression. Defaults to 0.
            second (int, optional): the second term of the progression. Defaults to 1.
        """
        super().__init__(first)         # start progression at first
        self._prev = second - first     # fictitious value preceding the first
        
    def _advance(self):
        """Update current value by taking sum of previous 2"""
        self._prev, self._current = self._current, self._prev + self._current

prog = Progression()
prog.print_progression(4)

arit = ArithmeticProgression(increment=4,start=0)
arit.print_progression(4)