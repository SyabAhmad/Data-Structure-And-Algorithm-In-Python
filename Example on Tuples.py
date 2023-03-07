# create a tuple
my_tuple = ('apple', 'banana', 'cherry')

# access elements of a tuple
print(my_tuple[0])   # output: 'apple'
print(my_tuple[1])   # output: 'banana'
print(my_tuple[2])   # output: 'cherry'

# loop through a tuple
for fruit in my_tuple:
    print(fruit)

# convert a tuple to a list
my_list = list(my_tuple)

# convert a list back to a tuple
my_new_tuple = tuple(my_list)

# concatenate two tuples
tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)   # output: ('a', 'b', 'c', 1, 2, 3)

# get the length of a tuple
print(len(my_tuple))   # output: 3

#In this example, we create a tuple called my_tuple
# with three elements:'apple', 'banana', and 'cherry'.
# We then accessindividual elements of the tuple using
# indexing,loop through the elements using a for loop,
# and convert the tuple to a list and back to a tuple.
#We also concatenate two tuples and get the length of a tuple.