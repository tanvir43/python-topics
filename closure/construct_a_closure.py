# Python closure is concept of enclosing and nested function
# using non local varibles to hold some value from the enclosed 
# function even after execution of the enclosed function

def enclosed_func(num):
    def nested_func(nested_num): # can use `num` from enclosed function
        return num * nested_num
    return nested_func

if __name__ == "__main__":
    res1 = enclosed_func(3)
    print(res1(5))

    res2 = enclosed_func(9)
    print(res2(2))