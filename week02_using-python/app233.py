import sys
# Week 2 - 2.3.3 More exercises with `if``

# Task - Practice `if` statements
# 1. Create a variable newStarter with value `John`.
# 2. Create a list variable nameList with values: `Kim`, `John`, `Hayden`, `Albert`, `Neelam`
# 3. Create an if comparison between the first element in the nameList list and the variable newStarter. 
#    If the values are the same, print `Found`.
# 4. Repeat this for the second element, third element and forth element in the list variable.

# 1. Create a variable newStarter with value `John`.
newStarter = "John"

# 2. Create a list variable nameList with values: `Kim`, `John`, `Hayden`, `Albert`, `Neelam`
nameList = ["Kim", "John", "Hayden", "Albert", "Neelam"]

# 3. Create an if comparison between the first element in the nameList list and the variable newStarter. 
#    If the values are the same, print `Found`.
if nameList[0] == newStarter:
    sys.stdout.write("Found at index 0 " + nameList[0] + "\n")

if nameList[1] == newStarter:
    sys.stdout.write("Found at index 1 " + nameList[1] + "\n")

if nameList[2] == newStarter:
    sys.stdout.write("Found at index 2 " + nameList[2] + "\n")

if nameList[3] == newStarter:
    sys.stdout.write("Found at index 3 " + nameList[3] + "\n")

if nameList[4] == newStarter:
    sys.stdout.write("Found at index 4 " + nameList[4] + "\n")

