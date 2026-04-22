import sys


# Implementation 1:

# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# print(num1+num2)


# Implementation 2: 

""" flush function needed here:

The following wont do shit because sys.stdout.write() does not automatically flush 
the output buffer, so the prompts may not appear before the user is expected to input
values.

"""
# WRONG WAY:

# sys.stdout.write("Enter number 1: ")
# num1 = int(sys.stdin.readline())
# sys.stdout.write("Enter number 2: ")
# num2 = int(sys.stdin.readline())
# sys.stdout.write(str(num1+num2))

# RIGHT WAY:

# sys.stdout.write("Enter number 1: ")
# sys.stdout.flush()
# num1 = int(sys.stdin.readline())
# sys.stdout.write("Enter number 2: ")
# sys.stdout.flush()
# num2 = int(sys.stdin.readline())
# sys.stdout.write(str(num1 + num2) + "\n")
