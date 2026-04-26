import sys

# Take two float inputs from user

# first number from the user
sys.stdout.write("Enter the first number: ")
num1 = float(sys.stdin.readline())

# second number from the user
sys.stdout.write("Enter the second number: ")
num2 = float(sys.stdin.readline())

# Add the two inputs together -> save to variable `total`
total = num1 + num2

# Dispaly the result of the calculation to the user
sys.stdout.write("The result is " + str(total) + "\n")
