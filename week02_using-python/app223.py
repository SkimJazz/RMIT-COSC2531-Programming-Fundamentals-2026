# Week 2: 2.2.3 - Using compound assignment operators
import sys

# EG.1 - Using Simple Assignment Operators
a = 3
b = a + 6
sys.stdout.write(str(b) + "\n")
sys.stdout.flush()
# Output: 9 => int

# EG.2 - Using Compound Assignment Operators
a = 3       # create variable `a` and assign it the value 3
b = a + 6       # create second variable `b` and assign it the value of `a` (3) + 6
sys.stdout.write(str(b) + "\n")
sys.stdout.flush()
# Output: 9 => int

# EG.2a - Using Compound Assignment Operators
b += a  # Apply compound operators `+=` to `b`, to make `b` take the value of `a`
sys.stdout.write(str(b) + "\n")
sys.stdout.flush()
# Output: 12 => int, `b` is now 9 + 3

# Test examples:

# TEST 1 - What is the value of `x`
x = 5
y = 10*2
x = y + x   # `x` takes the value of `y` (20) + `x` (5)
sys.stdout.write(str(x) + "\n")
sys.stdout.flush()
# Output: 25 => int, `x` is now 20 + 5


# TEST 2 - What is the final value of `z`
z = 12
y = 9/3
x = 1
z = z + y + x  # `z` takes the value of `z` (12) + `y` (3.0) + `x` (1)
z -= 2  # Apply compound operator `-=` to `z`, to make `z` take the value of `z` - 2
sys.stdout.write(str(z) + "\n")
sys.stdout.flush()
# Output: 14.0 => float, `z` is now 12 + 3.0 + 1 - 2




# TEST 3 - What is the value of `z`
x = 20
y = 3
z = x       # `z` takes the value of `x` (20)
x = x + 1   # `x` is now 21
z = x + z   # `z` takes the value of `x` (21) + `z` (20)
z *= 2      # Apply compound operator `*=` to `z`, to make `z` take the value of `z` * 2
sys.stdout.write(str(z) + "\n")
sys.stdout.flush()
# Output: 84 => int, `z` is now (21 + 20) * 2





# Eg.3 - Using Compound Assignment Operators with Different Operators