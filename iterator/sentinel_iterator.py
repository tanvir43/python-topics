# iter() function can have limit/sentinel

my_list = [1,3,5,2,9]

def my_func(my_list):
    return my_list

my_iterator = iter(int, 2) # this is not possible

res = next(my_iterator)
print(res) # 0

res = next(my_iterator)
print(res) # 0

res = next(my_iterator)
print(res) # 0

res = next(my_iterator)
print(res) # 0

res = next(my_iterator)
print(res) # 0 

res = next(my_iterator)
print(res) # 0

# the iterator becomes infinite because the the sentinal 2 
# can not be acheived by the result of `int` callable