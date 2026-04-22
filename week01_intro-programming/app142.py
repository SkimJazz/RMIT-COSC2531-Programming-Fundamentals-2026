# 1.4.2 Investigating error messages

import sys
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# print(num1/num2)

"""Output:
Enter number 1: 4
Enter number 2: 0
Traceback (most recent call last):
  File "app142.py", line 5, in <module>
    print(num1/num2)
          ~~~~^~~~~
ZeroDivisionError: division by zero
"""


# What is a ZeroDivisionError?
"""ZeroDivisionError

Exception raised when attempting to divide by zero.

A ZeroDivisionError occurs when the second argument of a division or modulo operation is zero.
This applies to both integer and floating-point divisions.

Example:
    num1 = 10
    num2 = 0
    result = num1 / num2  # Raises ZeroDivisionError: division by zero

Typical Causes:
    - Dividing any number by zero using /, //, or %.
    - User input that results in a zero denominator.

Handling the Error:
    try:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        print(num1 / num2)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

See Also:
    https: // docs.python.org/3/library/exceptions.html  # ZeroDivisionError

"""

# METHOD 1: What NOT to do!

# sys.stdout.write("Enter ID: ")
# roleID = int(sys.stdin.readline())
# sys.stdout.write("Enter ID "+str(roleID)+"'s role: ")
# role = sys.stdin.readline().strip()
# sys.stdout.write("Hello "+role+" 00"+str(roleID))


# METHOD 2: What NOT to do! But is slightly better than METHOD 1 because of the flush() function.

# sys.stdout.write("Enter ID: ")
# sys.stdout.flush()
# roleID = int(sys.stdin.readline())
# sys.stdout.write("Enter ID "+str(roleID)+"'s role: ")
# sys.stdout.flush()
# role = sys.stdin.readline().strip()
# sys.stdout.write("Hello "+role+" 00"+str(roleID))
# sys.stdout.flush()


# METHOD 3: The right way to do it! Using the built-in input() and print() functions.

roleID = int(input("Enter ID: "))
# Output: Enter ID: 1
role = input(f"Enter ID {roleID}'s role: ")
# Output: Enter ID 1's role: Admin
print(f"Hello {role} 00{roleID}")
# Output: Hello Admin 001
