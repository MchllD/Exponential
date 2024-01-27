# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.

# pseudocode

# create function to calculate the exponent of a given base and exponent
# Initialize the result to 1
# Loop through the range of the exponent
# Multiply the result by the base in each iteration

# Test cases
# Set values for the first test case

# ---------------------------------------- actual code ---------------------------------------------------

# create function to calculate the exponent of a given base and exponent
def exponent(base, exp):
    # Initialize the result to 1
    result = 1
    
    # Loop through the range of the exponent
    for _ in range(exp):
        # Multiply the result by the base in each iteration
        result *= base
        
    # Return the final result
    return result