"""
Iterator save resource.

The following example shows how an iterator 
can be design to iterate on without using any python memory

side effect: it is an infinite iterator
"""

class InfineIterator:

    def __iter__(self):
        self.counter = 2
        return self

    def __next__(self):
        result = self.counter
        self.counter += 2
        return result

if __name__ == "__main__":

    obj = InfineIterator() # we are taking input from __iter__ method
    my_iter = iter(obj)

    print(next(my_iter)) # 2
    print(next(my_iter)) # 4
    print(next(my_iter)) # 6
    print(next(my_iter)) # 8

# so on as its an infinite iterator