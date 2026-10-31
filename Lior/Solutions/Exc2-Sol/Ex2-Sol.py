# Copyright © 2026 Lior Brown
# All rights reserved.
#
# Created for: Introduction to Programming, Ariel University

############### Q1 ############
# This program gets from the user 2 numbers and an operator: [+,-,/,*] and outputs the result

# Get the first number (assuming valid number input)
num1 = float(input("Enter the first number: "))

# Get the operator
operator = input("Enter the operator (+, -, *, /): ")

# Re-prompt until the operator is one of the four valid operators
while operator != '+' and operator != '-' and operator != '*' and operator != '/':
    print(f"❌ Invalid operator '{operator}'.")
    operator = input("Enter the operator (+, -, *, /): ")

# Get the second number (assuming valid number input)
num2 = float(input("Enter the second number: "))

# Prevent division by zero - only relevant when the operator is '/'
while operator == '/' and num2 == 0:
    print("❌ Division by zero is not allowed.")
    num2 = float(input("Enter the second number: "))

# At this point the input is valid, so just calculate
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
else:
    result = num1 / num2

# Display the result
print(f"\nResult: {num1} {operator} {num2} = {result:.2f}")

############### Q2 ############
# This program simulates a day's eating schedule 😋
# The program gets from user 4 integers
#  1) Wake hour
#  2) Sleep hour
#  3) Fasting gap
#  4) Waiting time from meat to dairy (Can be zero, we are liberal 🤗)
#  (Ensure: 0 <= Wake hour < Sleep hour < 24)
# For each meal, the program asks: "the time is *****, what would you like to eat now?"
#  1) 'S' 🥩
#  2) 'P' 🍕
#  3) 'A' 🍎
# Validation: If the input is wrong or not allowed (violates constraints), the program prompts the user to choose again

# Get User's wake hour
wake_hour = int(input("Enter your wake hour (0-22): "))
while (not 0 <= wake_hour < 23):
    wake_hour = int(input("Please insert valid input (0-22): "))

# Get User's sleep hour
sleep_hour = int(input(f"Enter your sleep hour ({wake_hour + 1}-23): "))

while (not wake_hour < sleep_hour < 24):
    sleep_hour = int(input(f"Please insert valid input ({wake_hour + 1}-23): "))

# Get User's fasting gap
fasting_gap = int(input("Enter your fasting gap: "))

while (fasting_gap <= 0):
    fasting_gap = int(input(f"Please insert positive integer: "))

# Get User's waiting hours from meat do dairy
meat_to_dairy_wait = int(input("Enter your waiting time from meat to dairy: "))

while (meat_to_dairy_wait < 0):
    meat_to_dairy_wait = int(input("Please insert non-negative integer: "))

# 0 indicate that not eat meat
last_meat_time = None

print("\n--- Good morning 🌈 ---")

# The for loop iterates through all possible meal times (starting at wake_hour)
# and advances by the fasting_gap until the sleep_hour is reached.
# The 'hour' variable in the loop represents the CURRENT time for the meal.
for current_time in range(wake_hour, sleep_hour, fasting_gap):

    # Convert integer time to display format
    display_time = f"{current_time:02d}:00"

    is_valid = False

    # Meal Selection and Validation Loop
    while not is_valid:

        is_valid = True

        # Prompt the user
        print(f"\nThe time is {display_time}, what would you like to eat now?")
        food = input("'S': 🥩 | 'P': 🍕 | 'A': 🍎: ").upper()

        # If choose 🍕
        if food == 'P':
            # Checks if it violates constrain
            if (last_meat_time is not None and 
                current_time - last_meat_time < meat_to_dairy_wait):
                print(f"🛑 Constraint Broken: You must wait {meat_to_dairy_wait} " +
                      "hours after meat before having dairy.")
                is_valid = False

        # If choose 🥩
        elif food == 'S':
            last_meat_time = current_time

        # If choose invalid input
        elif food != 'A':
            print("❌ Invalid input. Please choose 'S', 'P', or 'A'.")
            is_valid = False

print("\n--- Good night 🌆 and Sleep tight 😴 ---")
