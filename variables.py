# Some rules for variables

# Your variable names cannot have spaces. Only use numbers, letters and underscores,
# such as: variable_num_1 = 5

# Some words are reserved by Python's coding language. An example of
# this is the word 'print'.

# Make your variable names descriptive but keep them short.

# A string type variable
my_string = "This is a string variable"
print(my_string)

# A number variable using an integer (int)
int_variable = 20
print(int_variable)

# A float variable
float_variable = 17.485
print(float_variable)

# You can reduce code by assigning values to multiple variables
# The value order must be the same as the variable name order
# so x =7, y=9, and i=19
x,y,i = 7,9,19
print(x,y,i)

# Here are some ways to use variables
# we create two variables with values 6 and 19
num_1 = 6
num_2 = 19
# We make another variable that will contain the result of num_1 * num_2
# ( the aserisk is multiplication in programming)
# We then make a new variable called sum, multiply num_1 and num_2, the result
# will be stored as the variable called sum, then we print it
sum = num_1 * num_2
print(sum)
# A shorter way to do this, is to use the print function
# and then multiply the numbers. As we are using the print
# function, it will print the result automatically.
print(num_1 * num_2)

# Subtraction
print(num_2 - num_1)

# Addition
print(num_1 + num_2)

# Division. Important, in programming, the symbol for division is /
print(num_2 / num_1)

# Here we can use a string variable
my_name = "simple syntax"
# We can print it using the print function
print(my_name)
# We can do other things though, using f strings. this allows
# some formatting for printing

# Here we add an f inside the (), and the variable inside the {}
# Python has a function called title which will capitalise first letters
# so we add the function using .title() after the variable name
# This results in Simple Syntax, instead of simple syntax
# Even though we created the string in lowercase, it is printed with capitalised letters
print(f"{my_name.title()}")

# Here are some other you can use with f strings
# All uppercase
print(f"{my_name.upper()}")

# Print all lowercase
print(f"{my_name.lower()}")

# Here we can change the variable entirely. Turning the
# string created in lowercase to all capitals then printing
# it using the standard print function
my_name = my_name.upper()
print(my_name)

# IMPORTANT! f-strings were introduced in Python version 3.6. Prior to this
# you would have to use the format() function. I strongly recommend updating
# to version 3.6 however to keep up to date

print(f"{my_string.lower()}")