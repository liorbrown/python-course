# Copyright © 2025 Lior Brown
# All rights reserved.
#
# Created for: Introduction to Programming, Ariel University

############### Q1 ############
# This program gets from the user 2 numbers and an operator: [+,-,/,*] and outputs the result

############### Q2 ############
# This program collects exam grades for a class and prints a summary 📊
# The program gets from the user:
#  1) The number of students (a positive integer)
#  2) A grade for each student (an integer between 0 and 100)
# For each student, the program asks: "Enter the grade of student #k: "
# Validation: If the input is out of range, the program prompts the user to enter it again
#
# After all grades are entered, the program outputs:
#  1) The average grade (rounded to 2 decimal places)
#  2) The highest and the lowest grade
#  3) How many students passed (grade >= 60) ✅ and how many failed ❌
#  4) If the average is below 70, suggest a factor 🎁:
#     the number of points to add to every grade so the average becomes exactly 70
#
# Note: Do not use lists! Compute everything while the grades are being entered.
#
# Example:
# Enter the number of students: 4
# Enter the grade of student #1: 55
# Enter the grade of student #2: 105
# Please insert a valid grade (0-100): 80
# Enter the grade of student #3: 60
# Enter the grade of student #4: 45
# Average: 60.00
# Highest: 80 | Lowest: 45
# Passed: 2 ✅ | Failed: 2 ❌
# Suggested factor: 10.00 points 🎁