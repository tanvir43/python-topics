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

    obj = InfineIterator() # we are not using any resource to store data
    my_iter = iter(obj)

    res = next(my_iter)
    print(res) # 2

    res = next(my_iter)
    print(res) # 4

    res = next(my_iter)
    print(res) # 6

    res = next(my_iter)
    print(res) # 8

# so on as its an infinite iterator