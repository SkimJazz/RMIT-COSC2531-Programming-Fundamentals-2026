import sys
# Week 2 - 2.2.6 Creating lists

colleagues = ["Sarah", "Sam", "Michael", "Andrew", "Jane"]
print(colleagues [0]) # Output: Sarah => string, the first item in the list `colleagues`
print(colleagues [1]) # Output: Sam => string, the second item in the list `colleagues`
print(colleagues [2]) # Output: Michael => string, the third item in the list `colleagues`
print(colleagues [3]) # Output: Andrew => string, the fourth item in the list `colleagues`
print(colleagues [4]) # Output: Jane => string, the fifth item in the list `colleagues`

# Printing beyond the last index of a list will error:
print(colleagues [5]) # Output: IndexError: list index out of range => error, there is no sixth item in the list `colleagues`
