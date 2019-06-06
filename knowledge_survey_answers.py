# These are programming questions to demonstrate how much you learned
# These questions are to be completed in 2 hours

# 1
# loop through the list given and print every item in the list

def loop_items(items):
    for i in range(items):
        print(items[i])

# 2
# take all the integers in a given list and multiply each by 2
# display the altered list

def mult_2(items):
    for i in range(items):
        items[i] = items[i] * 2
    print(items)


# 3
# take 2 strings and add them together
# return the result

def add_strings(string1, string2):
    print(string1 + string2)

# 4
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


# 5
# make a program which loops through the numbers 1-100
# if the number it is on is divisible by 3 and 5 print "fizzbuzz"
# if the number it is on is divisible by 3 print "fizz"
# if the number it is on is divisible by 5 print "buzz"
# if the number is not divisible by 3 and 5 then print the number

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)












def main():
    # results to check against
    # 1 -> prints 1, 2, 4, 8, 16, 32, 64
    # 2 -> prints 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
    # 3 -> prints hello world
    # 4 -> prints: 
    #           "you are young"
    #           "you are a kid"
    #           "you are a teenager"
    #           "you are a teenager and an adult"
    #           "you are an adult"
    #           "you are a senior citizen"
    # 5 -> prints 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz ......
    


    # uncomment lines below to run them

    # 1
    # loop_items([1, 2, 4, 8, 16, 32, 64])

    # 2
    # mult_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # 3
    # add_strings("hello", " world")

    # 4
    # age_commenter(1)
    # age_commenter(12)
    # age_commenter(13)
    # age_commenter(18)
    # age_commenter(50)
    # age_commenter(90)

    # 5
    # fizzbuzz()

    pass