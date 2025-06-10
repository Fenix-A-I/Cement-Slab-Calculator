'''
Concrete Slab Calculator
Goal: Refresh on using Python

References:
https://www.concretenetwork.com/concrete/howmuch/calculator.htm
'''

# Importing math module
import math

# Function to calculate the amount of cement in cubic yards
def calc_yards_cement (t, w, l):
    # Converting inches to feet
    # Multiplying thickness by width by length
    # Converting to cubic yards by dividing by pow(3, 3)
    # Rounding to 2 decimal places
    return round(((t/12) * w * l)/(pow(3, 3)), 2)

# Function to print the results
def print_results(t, w, l):
    print("\n\033[92m A cement slab", str(t),"inches thick,", str(w),"ft wide and", str(l),"ft long requires", calc_yards_cement(t, w, l) ,"cubic yards of cement.\033[0m\n")

print("\n========== Concrete Slab Calculator ==========\n")
# Initializing variables for thickness, width, and length
thickness = None
width = None
length = None

# Outer try-except block to handle keyboard interrupts
try:
    # Input loop for thickness, width, and length
    while thickness is None:
        try:
            thickness = float(input("- Enter the thickness of the cement in inches: "))
            # Checking if the input is a positive number
            if thickness <= 0:
                print("\033[91m Invalid input. Thickness must be a positive number.\033[0m\n")
                thickness = None
        # Catching ValueError if the input is not a number
        except ValueError:
            print("\033[91m Invalid input. Please enter a numeric value.\033[0m\n")

    # Input loop for width
    while width is None:
        try:
            width = float(input("- Enter the width of the cement in ft: "))
            # Checking if the input is a positive number
            if width <= 0:
                print("\033[91m Invalid input. Width must be a positive number.\033[0m\n")
                width = None
        # Catching ValueError if the input is not a number
        except ValueError:
            print("\033[91m Invalid input. Please enter a numeric value.\033[0m\n")

    # Input loop for length
    while length is None:
        try:
            length = float(input("- Enter the length of the cement in ft: "))
            # Checking if the input is a positive number
            if length <= 0:
                print("\033[91m Invalid input. Length must be a positive number.\033[0m\n")
                length = None
        # Catching ValueError if the input is not a number
        except ValueError:
            print("\033[91m Invalid input. Please enter a numeric value.\033[0m\n")

    print_results(thickness, width, length)
# If the user interrupts the program, catch the exception and exit gracefully
except KeyboardInterrupt:
    print("\n\033[93m Program interrupted. Exiting gracefully.\033[0m\n")
