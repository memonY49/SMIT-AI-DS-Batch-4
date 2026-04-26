# Funtion: It is a block of code seperated from atmosphare to perform individual task.
# types of functions:
# 1. pre defined (print,len,input,...)
# 2. user defined 
# To create a user defined function:
# syntax:
#   def name_of_the_function(     ):
#       body of function.
# call a function:
# syntax:
#   name_of_the_function()


# def add():
#     a = 3
#     b = 5
#     print(a+b)

# add()


# Parameters:
#     1. required parameters
#     2. key parameters (optional)


def add(x=0, y=5):
    print(x+y)

# def sub(x,y):
#     print(x-y)
# add(4,10)
# add(4,10)
# add(4,10)


# return value:
# `    

def sub(x,y):
    return x-y


value = sub(5,6)

print(value*2)