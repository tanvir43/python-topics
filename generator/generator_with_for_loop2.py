"""
Generator using for loop.

Extract items using `for` loop of a generator
"""

def my_generator(m):
    """
    param m: maximum range
    """

    my_list = list()
    for i in range(0, m):
        value = i ** 2
        my_list.append(value)
        yield my_list

if __name__ == "__main__":
    for result in my_generator(10):
        print(result)
        # output:
        # [0]
        # [0, 1]
        # [0, 1, 4]
        # [0, 1, 4, 9]
        # [0, 1, 4, 9, 16]
        # [0, 1, 4, 9, 16, 25]
        # [0, 1, 4, 9, 16, 25, 36]
        # [0, 1, 4, 9, 16, 25, 36, 49]
        # [0, 1, 4, 9, 16, 25, 36, 49, 64]
        # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]