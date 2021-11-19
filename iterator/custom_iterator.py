# custom iterator

class Squares:
    """
    An iterator class

    Construct a square iterator i.e
    each iteration will give a square result
    """
    def __init__(self, max_limit):
        self.max = max_limit

    def __iter__(self):
        self.pos = 0
        return self

    def __next__(self):
        if self.pos < self.max:
            result = self.pos ** 2
            self.pos += 1
            return result
        else:
            raise StopIteration

if __name__ == "__main__":
    obj = Squares(5)
    square = iter(obj)

    res = next(square)
    print(res) # 0

    res = next(square) 
    print(res) # 1

    res = next(square)
    print(res) # 4

    res = next(square)
    print(res) # 9

    res = next(square)
    print(res) # 16 

    res = next(square)
    print(res) # raise StopIteration