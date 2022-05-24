

"""
    Iterators and Generators
    iterator vs iterable
    Most convenient technique for creating iterators in Python is through the use of generators
    Instead of returning values, a yield statement is exeecuted to indicate each element 
    of the series
    Generator syntax is particularly attractive when results do no need to be stored in memory
    E.g total = sum(k*k for k in range(1, n+1))
"""

from re import A


data = [1, 2, 3, 4]
#next(data) illegal
i = iter(data)
data[2] = 9
print(i)
print(next(i))
print(next(i))
data[3] = 'c'
print(next(i))
print(next(i))

def factors(n):
    results = [] # Store factures in a new list
    for k in range(1, n+1): 
        if not n%k:
            results.append(k)
    return results

print(factors(100))

def generator_factors(n): # generator that computes factors
    """_summary_
    replaced return with yield -> we are defining a generator rather than a traditional factor
    Not possible to combine return and yield
    

    Args:
        n (_type_): _description_

    Yields:
        _type_: _description_
    """
    for k in range(1,n+1):
        if not n%k:
            yield k # yield this factor as next result
            
def generator_factors_optimized(n):
    k = 1
    while k*k < n:
        if not n%k:
            yield k
            yield n // k
            print(n // k,k)
        k += 1
    if k * k == n:
        yield k
        
def fibonacci():
    a = 0
    b = 1
    while True:
        yield a 
        a, b = b, a + b # More effective
        '''
        future = a + b
        a = b
        future = b
        '''        
            

aux = generator_factors_optimized(100)
aux2 = list(aux)
print(aux2)


l = [k*k for k in range(1,10)]     # list comprehension
s = {k *k for k in range(1,10)}    # set comprehension
g = (k*k for k in range(1,10))     # generator comprehension
d = {k: k*k for k in range(1,10)}  # dictionary comprehension