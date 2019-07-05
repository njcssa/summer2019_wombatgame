# To do with instructors:

# create 5 variables which all hold different types of data
# at least 1 should hold an int
# at least 1 should hold a double
# at least 1 should hold a boolean
# at least 1 should hold a string
# 1 variable can hold whatever you want
# then print out what one variable holds

var1 = 1
var2 = 1.23
var3 = True
var4 = "bobby"
var5 = "hi world"

print(var4)


# make a program which comments on peoples' age
# if they are younger than 5 print "you are young"
# if they are between 6 and 12 print "you are a kid"
# if they are between 13 and 19 print "you are a teenager"
# if they are 18 or 19 print "you are a teenager and an adult"
# if they are between 20 and 64 print "you are an adult"
# if they are 65 or older, print "you are a senior citizen"

def age_commenter(age):
    if age <= 5:
        print("you are young")
    elif age >= 6 and age <= 12:
        print("you are a kid")
    elif age == 19 or age == 18:
        print("you are a teenager and an adult")
    elif age >= 13 and age <= 19:
        print("you are a teenager")
    elif age >= 20 and age <= 64:
        print("you are an adult")
    elif age >= 65:
        print("you are a senior citizen")


# make 4 if statements
# 1 should have a not
# 1 should have an and
# 1 should have an or
# 1 should combine at least 2 of an and, or, not

def if_statements():
    var1 = 5
    var2 = 10
    var3 = "ben"
    var4 = False

    if var1 < 10 and var1 > 1:
        print("var1 is between 1 and 10")
    
    if not var4:
        print("changed False to True")
    
    if var3 == "ben" or var1 < 3:
        print("at least one of these is True")
    
    if not(var3 == "ben" or var1 > 4):
        print("something")


# make a while loop that prints the numbers 1-10

def print_ten():
    i = 1
    while i <= 10:
        print(i)
        i += 1


# make a while loop that counts by twos

def count_by_two():
    i = 0
    while i < 20:
        print(i)
        i += 2


# make a while loop that loops through the number 1-10
# only print out numbers if they are greater than 5

def print_greater_than_five():
    i = 1
    while i <= 10:
        if i > 5:
            print(i)
        i += 1


# make a function that takes two parameters that are ints
# inside the function have it print out the sum
# remember to call the function

def add(a, b):
    print(a + b)

add(1, 2)

# make a function that takes two parameters that are ints
# inside the function have it return the sum
# remember to call the function
# now call the function within the add2 function

def add2(a, b):
    return(a + b)

add2(add2(1, 1), add2(4, 2))


# make a function that returns a list of even numbers in a certain range
# print the returned list

def get_evens(start, end):
    evens_list = []
    i = start
    while i < end:
        evens_list.append(i)
        i += 2
    return evens_list

print(get_evens(2, 19))


# make a function which takes a list of ints as an input
# have the function return a list with every value in the original list doubled

def double_list(sl):
    new_list = []
    i = 0
    while i < len(sl):
        new_list.append(sl[i] * 2)
        i += 1
    return new_list

new_list = double_list([1, 2, 3, 4, 5, 6])

# alternate version that deals with lists and references

def double_list2(sl):
    i = 0
    while i < len(sl):
        sl[i] = sl[i] * 2
        i += 1

some_list = [1, 2, 3, 4, 5, 6]
double_list2(some_list)
print(some_list)

# lists are special though because this doesn't work with other types of variables

def reference_example(i):
    i = i * 2

i = 5
reference_example(i)
print(i)

# make a function which bubble sorts a list

def bubble_sort(li):
    current_index = 0
    i = 0
    while current_index < len(li):
        while i < len(li) - current_index - 1:
            if li[i] > li[i+1]:
                temp = li[i+1]
                li[i+1] = li[i]
                li[i] = temp
            i += 1
        current_index += 1
        i = 0

li = [2, 6, 5, 1, 3, 10, 9, 11]
bubble_sort(li)
print(li)



# To do by yourself:


# make a function which takes a list as a parameter
# return the smallest number

def get_smallest(li):
    i = 0
    smallest = li[0]
    while i < len(li):
        if li[i] < smallest:
            smallest = li[i]
        i += 1
    return smallest

li = [2, 5, 1, 76, 89, 0, 3]
print(get_smallest(li))

# make a function which calculates a number to a power
# return the answer

def power(a, b):
    answer = 1
    i = 0
    while i < b:
        answer *= a
    return answer

print(power(5, 5))


# Make a function which takes in a list of integers as a parameter.
# return the number of even integers in the list.

list1 = [22, 32, 55, 90, 24, 67]

def count_evens(l):
    count = 0
    for i in range(len(l)):
        if l[i] % 2 == 0:
            count += 1
    return count

print(count_evens(list1))


        
