import sys
# Week 2 - 2.2.5 Manipulating strings in Python

# Topics:
#   - Working with `String` (str) functions
#   - Change letters to Upper or Lower case
#   - Finding the length of a string
#   - Concatenating, Merging, or Joining strings together
#   - Splitting Strings


# Apparently, these are some of the most useful string functions in Python:
# count()
# endswith()
# find()
# index()
# join()
# lower()
# replace()
# split()
# upper()

# EXAMPLE - Using `str` functions
s1 = "aba abraham bred buce cat coffee"
s2 = "Alex"
s3 = "Fergusen"

# Use the "Useful" string functions to manipulate the strings `s1`, `s2`, and `s3` as per
# the instructions below.


# EG.1 - Change the letters in `s2` to all upper case.
s2_upper = s2.upper()
print(s2_upper)
# Output: ALEX => string, `s2` is now "ALEX"


# EG.2 - Split `s1` into multiple sub-strings separated by spaces.
s1_split = s1.split()
print(s1_split)
# Output: ['aba', 'abraham', 'bred', 'buce', 'cat', 'coffee'] => list of strings, `s1` is now a list of sub-strings


# EG.3 - Check and see if `s1` ends with a full stop.
s1_ends_with_period = s1.endswith('.')
print(s1_ends_with_period)
# Output: False => boolean, `s1` does not end with a full stop


# EG.4 - Print the number of "aba" that exist in variable `s1`. 
#   WTF?: It should say "Print the number of times "aba" occurs in variable `s1`."
s1_aba_count = s1.count("aba")
print(s1_aba_count)
# Output: 1 => int, there is one occurrence of "aba" in `s1`


# EG.5 - Print the index number of "bred" in variable `s1`.
#   again WTF?: You can't print the index number in `s1`, as `s1 is a string, not a list. You can only
#   print the index number of "bred" in the list `s1_split`, which is the result of splitting `s1` into
#   sub-strings (A fuckn LIST of STRINGS, not a string).

s1_bred_index = s1_split.index("bred")
print(s1_bred_index)
# Output: 2 => int, "bred" is at index 2 in the list `s1_split`


# EG.6 - Count the number of "a" in `s1`.
s1_a_count = s1.count("a")
print(s1_a_count)
# Output: 6 => int, there are 6 occurrences of "a" in `s1`


# EG.7 - Add a space between all characters in `s2`.
s2_with_spaces = ' '.join(s2)
print(s2_with_spaces)
# Output: A L E X


# EG.8 - Replace all `b` in `s1` with upper case `B`.
s1_b_replaced = s1.replace('b', 'B')
print(s1_b_replaced)
# Output: aBa aBraham Bred Buce cat coffee
