# Prerequisites: Yield Keyword and Iterators
# When to use yield instead of return in Python?
"""
The yield statement suspends function’s execution and sends a value back to the caller,
but retains enough state to enable function to resume where it is left off. When resumed,
the function continues execution immediately after the last yield run.
This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list.

Let’s see with an example:
"""
# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)


# A Python program to demonstrate use of
# generator object with next()

# A generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# x is a generator object
x = simpleGeneratorFun()

# Iterating over the generator object using next
print(x.next());  # In Python 3, __next__()
print(x.next());
print(x.next());


# A Python program to generate squares from 1
# to 100 using yield and therefore generator

# An infinite generator function that prints
# next square number. It starts with 1
def nextSquare():
    i = 1;

    # An Infinite loop to generate squares
    while True:
        yield i * i
        i += 1  # Next execution resumes
        # from this point


# Driver code to test above generator
# function
for num in nextSquare():
    if num > 100:
        break
    print(num)
