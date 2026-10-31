# Copyright © 2026 Lior Brown
# All rights reserved.
#
# Created for: Introduction to Programming, Ariel University

############### Q1 ############
# Guess the number 🎯
# The secret number is YOUR year of birth 🎂 (define it as a constant at the top of the program)
# The user has 7 attempts to guess a year between 1900 and 2026
# After each guess the program prints: "Too high!" 📉 or "Too low!" 📈
# Correct guess - print in which attempt the user succeeded
# Out of attempts - reveal the secret number
# Validation: A guess out of range (1900-2026) - print an error and ask again, WITHOUT losing an attempt

############### Q2 ############
# ATM 🏧
# The PIN is YOUR year of birth 🎂 and the starting balance is 1000
# The user has 3 attempts to enter the PIN. 3 mistakes - the card is blocked 🔒 and the program ends
# After a correct PIN, a menu is shown again and again until the user chooses to exit:
#  1) Balance 💰
#  2) Deposit 📥
#  3) Withdraw 📤
#  4) Exit 👋
# Validation:
#  - Invalid choice (not 1-4) - print an error and go back to the menu
#  - Withdraw - a positive amount, in multiples of 50, and not more than the balance. Otherwise - print an error

############### Q3 ############
# Perfect numbers 🌟
# A perfect number is a number that equals the sum of its divisors (not including itself)
# For example: 6 = 1 + 2 + 3
# The program gets an integer N and prints all the perfect numbers up to N - each one with its divisors
# At the end, the program prints how many perfect numbers were found
# Validation: N must be greater than 1 - otherwise print an error and ask again

############### Q4 ############
# Collatz conjecture 🪜
# Start from a positive number and repeat the rule until reaching 1:
#  - Even:  n // 2
#  - Odd:   3 * n + 1
# For example: 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 (8 steps)
# The program gets an integer N, prints for each number from 1 to N how many steps it took to reach 1,
# and at the end announces the champion - the number with the most steps 🏆
# Validation: N must be positive - otherwise print an error and ask again
