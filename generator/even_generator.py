"""
Create an even iterator using generator

A fucntion is considered a generator when it use at least
one `yeild` statement instead of return
"""

def even_generator():
    """
    Generator example

    The `yeild` statement don't terminate the function
    rather pause the function and save the state to use
    it in the next successive calls
    """
    n = 2
    yield n

    n +=2
    yield n

    n +=2
    yield n

    n +=2
    yield n

    n +=2
    yield n


if __name__ == "__main__":
    my_generator = even_generator() # storing the iter object in `my_generator`

    # getting the iterated item(one at a time) by `next`
    print(next(my_generator)) # 2
    print(next(my_generator)) # 4
    print(next(my_generator)) # 6
    print(next(my_generator)) # 8
    print(next(my_generator)) # 10
    print(next(my_generator)) # error(StopIteration)