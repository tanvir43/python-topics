# When a python function take another function as an argument
# then that function is called higher order function


# A higher order function
def higher_order_function(func):
    return func

def my_func():
        print("This is my function")

if __name__ == "__main__":
    higher_order_function(my_func())