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

# Test cases
# Set values for the first test case
base1, exp1 = 4, 6
result1 = exponent(base1, exp1)
print(f"{base1} raises to the power of {exp1} is: {result1}")


# Set values for the second test case
base2, exp2 = 5, 4
result2 = exponent(base2, exp2)
print(f"{base2} raises to the power of {exp2} is: {result2}")

