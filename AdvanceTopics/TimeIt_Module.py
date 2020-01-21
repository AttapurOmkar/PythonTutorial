# This module provides a simple way to find the execution time of small bits of Python code.

# Example 1

# importing the required module
import timeit

# code snippet to be executed only once
mysetup = "from math import sqrt"

# code snippet whose execution time is to be measured
mycode = ''' 
def example(): 
    mylist = [] 
    for x in range(100): 
        mylist.append(sqrt(x)) 
'''

# timeit statement
print
timeit.timeit(setup=mysetup,
              stmt=mycode,
              number=10000)

# Example


timeit.timeit("print('-'.join(str(n) for n in range(100)))",number=100)