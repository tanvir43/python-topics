# This is an example of simple decorator

def decorate(func):
    def inner():
        print("Logger added")
        func()
    return inner

def my_func():
    print("Morning learner")

if __name__ == "__main__":
    my_func() # before decorated
    decorated = decorate(my_func) # decorate `my_func`
    decorated() # after decorated