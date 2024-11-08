#------------------------------------------------------------------------------------
#Task 1: Function with Loop and Conditional Logic

# TODO: Define a function called 'check_attendance' that takes a list of names (students) and a list of absentees.
#       It should return a list of names of students who are absent.

def check_attendance(students, absentees):
    return{student for student in students if student in absentees}

# # TODO: Call 'check_attendance' with a list of ["Alice", "Bob", "Charlie", "David"] 
#       and a list of absentees ["Bob", "David"], and print the result.
students = {'Alice', 'Bob', 'Charlie', 'David'}
absentees = ['Bob', 'David']

for student in students:
    for absent in absentees:
        if student == absent:
            print(absent)

# ------------------------------------------------------------------------------------
# Task 2: Function for Real-Life Data Processing

# TODO: Define a function called 'calculate_average_grade' that takes a dictionary where the keys are student names 
#       and the values are their grades, and returns the average grade of the class.

def calculate_avg_grade(grades):
    total = sum(grades.values())  
    count = len(grades)            
    average = total / count       


# TODO: Call the 'calculate_average_grade' function with the following dictionary:
#       {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}, and print the result.

student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}
average_grade = calculate_avg_grade(student_grades)
print(f"The average grade of the class is: {calculate_avg_grade}")

#-----------------------------------------------------------------------------------------
# Task 3: Function Returning a Function (Higher-Order Function)

# TODO: Define a function called 'operation_selector' that takes a string "add" or "multiply" as a parameter,
#       and returns a function that either adds or multiplies two numbers.
def operation_selector(operation):
    if operation == "add":
        return lambda x, y: x + y
    elif operation == "multiply":
        return lambda x, y: x * y
    else:
        raise ValueError("Invalid operation. Use 'add' or 'multiply'.")

# TODO: Use 'operation_selector' to get the "add" function, and then call it to add 4 and 6.
add_function = operation_selector("add")
result_add = add_function(4, 6)
print(f"4 + 6 = {result_add}")

# TODO: Use 'operation_selector' to get the "multiply" function, and then call it to multiply 3 and 7.
multiply_function = operation_selector("multiply")
result_multiply = multiply_function(3, 7)
print(f"3 * 7 = {result_multiply}")

#------------------------------------------------------------------------------------
# Task 4: Function for a Practical Scenario

# TODO: Define a function called 'calculate_trip_cost' that takes three parameters:
# • distance (in km), fuel_efficiency (km per liter), fuel_price (price per liter),
# • and returns the total cost of fuel for the trip.
# Task : Using a for loop with a dictionary (Real-life Scenario: Grocery Shopping List)
def calculate_trip_cost(distance, fuel_efficiency, fuel_price):
    """Calculate the total cost of fuel for a trip."""
    liters_needed = distance / fuel_efficiency  
    total_cost = liters_needed * fuel_price     
    return total_cost

# TODO: Create a dictionary with grocery items as keys and their quantities in stock as values.
grocery_inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Tomatoes": 25,
    "Bread": 15,
    "Milk": 10
}

# TODO: Use a for loop to print each item and its quantity in stock.
print("\nGrocery Inventory:")
for item, quantity in grocery_inventory.items():
    print(f"{item}: {quantity} in stock")

# TODO: Calculate and print the total number of items in stock (sum of all values in the dictionary).
total_items = sum(grocery_inventory.values())
print(f"\nTotal number of items in stock: {total_items}")

#------------------------------------------------------------------------------------
# Task 5: Using a while loop for banking (Real-life Scenario: ATM Pin Retry System)
correct_pin = "1234"
attempts = 0
max_attempts = 3

# TODO: Ask the user to input their PIN.
while attempts < max_attempts:
    user_pin = input("Please enter your PIN: ")

# TODO: If the PIN is incorrect, ask the user to try again, but only allow 3 attempts.
if user_pin == correct_pin:
        print("Access Granted.")
        
else:
    attempts += 1
    print(f"Incorrect PIN. You have {max_attempts - attempts} attempts left.")

# TODO: After 3 incorrect attempts, print "Account Locked". If the PIN is correct, print "Access Granted".

correct_pin = "1234"
attempts = 0

# TODO: Use a while loop to implement the retry system.
if attempts == max_attempts:
    print("Account Locked.")

#------------------------------------------------------------------------------------
# Task 6: Using a for loop with range() for a School Grading System

# TODO: Create a list with 10 random assignment scores (between 0 and 100).
scores = [random.randint(0, 100) for _ in range(10)]

# TODO: Use a for loop to calculate the total score.
total_score = 0
for score in scores:
    total_score += score

# TODO: Calculate and print the average score for the class.
average_score = total_score / len(scores)

print("Assignment Scores:", scores)
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score:.2f}")

# Bonus: Use conditional logic to print a congratulatory message if the average is above 75.
if average_score > 75:
    print("Congratulations! The class average is above 75!")

import random

# List of 10 student scores.
scores = [random.randint(0, 100) for _ in range(10)]

# TODO: Calculate total and average scores.
average_score = total_score / len(scores)

#------------------------------------------------------------------------------------
# Task 7: Using the random module (Real-life Scenario: Random Team Selection)

# TODO: Create a list with the names of 20 participants.
participants = [
    "Alice", "Bob", "Charlie", "David", "Eva", 
    "Frank", "Grace", "Hannah", "Ian", "Jack",
    "Kathy", "Liam", "Mia", "Noah", "Olivia",
    "Paul", "Quinn", "Rachel", "Steve", "Tina"
]

# TODO: Use the random module to select 5 random participants.
selected_team = random.sample(participants, 5)

# TODO: Print the names of the selected team members.
print("Selected team members:")
for member in selected_team:
    print(member)

    
import random

# List of participants.
participants = ["Person1", "Person2", "Person3", ..., "Person20"]

# TODO: Randomly select 5 people from the participants list.


#------------------------------------------------------------------------------------
# Task 8: Custom module for a Fitness Tracker (Real-life Scenario: Tracking Calories Burned)

# Step 1: Create a module named 'fitness_tracker.py' with the following functions:
"""
def walk_calories(distance_km):
    # Calories burned per km walking: 50
    return distance_km * 50

def run_calories(distance_km):
    # Calories burned per km running: 100
    return distance_km * 100

def cycle_calories(distance_km):
    # Calories burned per km cycling: 70
    return distance_km * 70
"""
#------------------------------------------------------------------------------------
# Step 9: Use the custom module in your main script:

# TODO: Import the custom 'fitness_tracker' module.
import fitness_tracker 

# TODO: Ask the user to input the distance they walked, ran, and cycled today.
distance_walked = float(input("Enter the distance walked (in km): "))
distance_ran = float(input("Enter the distance ran (in km): "))
distance_cycled = float(input("Enter the distance cycled (in km): "))

# TODO: Calculate and print the total calories burned for each activity.
calories_walked = fitness_tracker.walk_calories(distance_walked)
calories_ran = fitness_tracker.run_calories(distance_ran)
calories_cycled = fitness_tracker.cycle_calories(distance_cycled)

# TODO: Sum and print the total calories burned for the day.
print(f"Calories burned walking: {calories_walked} kcal")
print(f"Calories burned running: {calories_ran} kcal")
print(f"Calories burned cycling: {calories_cycled} kcal")

#------------------------------------------------------------------------------------
# Task 10: Using a while loop to Simulate Loan Repayment (Real-life Scenario: Paying Off a Loan)

# TODO: Ask the user to input the total loan amount.
loan_amount = float(input("Enter the total loan amount: "))

# TODO: Ask the user to input their monthly repayment amount.
monthly_payment = float(input("Enter your monthly payment amount: "))

# TODO: Use a while loop to simulate monthly payments, reducing the loan each month.
if monthly_payment <= 0:
    print("Monthly payment must be greater than zero.")
elif monthly_payment >= loan_amount:
    print("You can pay off the loan in one payment!")
else:
    while loan_amount > 0:
        loan_amount -= monthly_payment
        if loan_amount < 0:
            loan_amount = 0  # Ensure the loan amount doesn't go negative
        print(f"Remaining loan amount: ${loan_amount:.2f}")

# TODO: Print the remaining loan amount after each payment.
print("Congratulations! You have fully paid off your loan!")

# TODO: When the loan is fully paid off, print a congratulatory message.

loan_amount = float(input("Enter the total loan amount: "))
monthly_payment = float(input("Enter your monthly payment amount: "))

# TODO: Use a while loop to simulate the repayment process.
while loan_amount > 0:
        loan_amount -= monthly_payment