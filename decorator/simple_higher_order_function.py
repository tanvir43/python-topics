"""
Higher order function:

A higher order function is a function which takes another function as an arguments
"""

def inc(x):
    return x + 1

def dec(y):
    return y - 1


def operator(func, x=None):
    """
    A simple example of higher order function
    """
    if x is None:
        x = 0
    result = func(x)
    return result

if __name__ == "__main__":
    inc_result = operator(inc, 2)
    dec_result = operator(dec, 4)
    print("incremented result", inc_result)
    print("decremented result", dec_result)



