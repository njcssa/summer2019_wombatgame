# To do with instructors:

# create 5 variables which all hold different types of data
# at least 1 should hold an int
# at least 1 should hold a double
# at least 1 should hold a boolean
# at least 1 should hold a string
# 1 variable can hold whatever you want
# then print out what one variable holds



# make a program which comments on peoples' age
# if they are younger than 5 print "you are young"
# if they are between 6 and 12 print "you are a kid"
# if they are between 13 and 19 print "you are a teenager"
# if they are 18 or 19 print "you are a teenager and an adult"
# if they are between 20 and 64 print "you are an adult"
# if they are 65 or older, print "you are a senior citizen"

def age_commenter(age):
    pass


# make 4 if statements
# 1 should have a not
# 1 should have an and
# 1 should have an or
# 1 should combine at least 2 of an and, or, not

def if_statements():
    pass


# make a while loop that prints the numbers 1-10

def print_ten():
    pass


# make a while loop that counts by twos

def count_by_two():
    pass


# make a while loop that loops through the number 1-10
# only print out numbers if they are greater than 5

def print_greater_than_five():
    pass


# make a function that takes two parameters that are ints
# inside the function have it print out the sum
# remember to call the function

def add(a, b):
    pass

add(1, 2)

# make a function that takes two parameters that are ints
# inside the function have it return the sum
# remember to call the function
# now call the function within the add2 function

def add2(a, b):
    pass

add2(add2(1, 1), add2(4, 2))


# make a function that returns a list of even numbers in a certain range
# print the returned list

def get_evens(start, end):
    pass

print(get_evens(2, 19))


# make a function which takes a list of ints as an input
# have the function return a list with every value in the original list doubled

def double_list(sl):
    pass

new_list = double_list([1, 2, 3, 4, 5, 6])

# alternate version that deals with lists and references

def double_list2(sl):
    pass

some_list = [1, 2, 3, 4, 5, 6]
double_list2(some_list)
print(some_list)

# lists are special though because this doesn't work with other types of variables

def reference_example(i):
    pass

i = 5
reference_example(i)
print(i)

# make a function which bubble sorts a list

def bubble_sort(li):
    pass

li = [2, 6, 5, 1, 3, 10, 9, 11]
bubble_sort(li)
print(li)



# To do by yourself:


# make a function which takes a list as a parameter
# return the smallest number

def get_smallest(li):
    pass

li = [2, 5, 1, 76, 89, 0, 3]
print(get_smallest(li))

# make a function which calculates a number to a power
# return the answer

def power(a, b):
    pass

print(power(5, 5))


# Make a function which takes in a list of integers as a parameter.
# return the number of even integers in the list.

list1 = [22, 32, 55, 90, 24, 67]

def count_evens(l):
    pass

print(count_evens(list1))


        
