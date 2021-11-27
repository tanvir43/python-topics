# example of calling a closure inside another 
# closure funtion

def enclosed_func(num):
    def nested_func(nested_num): # can use `num` from enclosed function
        return num * nested_num
    return nested_func

if __name__ == "__main__":
    res1 = enclosed_func(3)
    res2 = enclosed_func(9)
    print(res2(res1(2)))