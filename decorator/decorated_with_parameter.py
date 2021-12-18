 # An example of decorating a function which have parameters

def valid_parameter(func):
    def inner(a, b):
        if b > 0:
           return func(a, b)
        else:
            print("devider can not be 0")
            return "success"
    return inner

@valid_parameter
def divide(a, b):
     return a/b

if __name__ == "__main__":
    print(divide(4,2))

