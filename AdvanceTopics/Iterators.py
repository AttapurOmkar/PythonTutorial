"""
Iterator in python is any python type that can be used with a ‘for in loop’. Python lists, tuples, dicts and sets are all examples of inbuilt iterators.
These types are iterators because they implement following methods. In fact, any object that wants to be an iterator must implement following methods.

__iter__ method that is called on initialization of an iterator. This should return an object that has a next or __next__ (in Python 3) method.
 next ( __next__ in Python 3) The iterator next method should return the next value for the iterable. When an iterator is used with a ‘for in’ loop, the for loop implicitly calls next() on the iterator object.
 This method should raise a StopIteration to signal the end of the iteration.

 Below is a simple Python program that creates iterator type that iterates from 10 to given limit.
 For example, if limit is 15, then it prints 10 11 12 13 14 15. And if limit is 5, then it prints nothing.

"""


# A simple Python program to demonstrate
# working of iterators using an example type
# that iterates from 10 to given value

# An iterable user defined type
class Test:

    # Cosntructor
    def __init__(self, limit):
        self.limit = limit

        # Called when iteration is initialized

    def __iter__(self):
        self.x = 10
        return self

    # To move to next element. In Python 3,
    # we should replace next with __next__
    def next(self):
        # Store current value ofx
        x = self.x

        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration

            # Else increment and return old value
        self.x = x + 1;
        return x

    # Prints numbers from 10 to 15


for i in Test(15):
    print(i)

# Prints nothing
for i in Test(5):
    print(i)

