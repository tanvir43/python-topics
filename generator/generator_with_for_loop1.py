"""
Generator using for loop.

Extract items using `for` loop of a generator
"""

def my_generator(m):
    """
    param m: maximum range
    """
    number = 0
    while number <= m:
        value = number ** 2
        yield value
        number += 1

if __name__ == "__main__":
    for result in my_generator(10):
        print(result) # 0 2 4 9 16 25 .......