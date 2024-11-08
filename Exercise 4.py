# Question 1: Using a for loop with a list

# TODO: Create a list of fruits

fruit_list = ["Strawberry", "Blackberry", "Coconut", "Peach", "Watermelon", "Apple", "Litchi"]

# TODO: Use a for loop to print each fruit in the list

for fruit in fruit_list:
    print(fruit)

# -------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1

count = 5
while count > 0:
    print(count)
    
    count -= 1#decrement

# -------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers

for square in range(1, 11):
    print(square** 2)

# -------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module

import random

# TODO: Create a list of colors

colour_list = ["Black", "White", "Red", "Green", "Purple", "Blue","Yellow", "Pink"]

# TODO: Use a for loop to select and print 3 random colors from the list

for colour in range(3):
    print(random.choice(colour_list))

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions

import math_operations as mo

# TODO: Use a while loop to create a simple calculator

def calculator():
    while True:
        
operation = input("Enter a function here: ")

num1 = int(input("Enter a 1st number: "))
num2 = int(input("Enter a 2nd number: "))

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
else:
    print(num1 / num2)

