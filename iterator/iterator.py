# Python iterator
# List, tuple, string, dictionary are the iterators

#example
a = [1,2,3,4,5]

# use __iter__ and __next__ magic methods to make `a` an iterator

my_iterator = iter(a) # iter() calls __iter__ implicitly
item = next(my_iterator)
print(item) # 1

item = next(my_iterator)
print(item) # 2

item = next(my_iterator)
print(item) # 3

item = next(my_iterator)
print(item) # 4

item = next(my_iterator)
print(item) # 5

item = next(my_iterator)
print(item) # raise `stop iteration` exception