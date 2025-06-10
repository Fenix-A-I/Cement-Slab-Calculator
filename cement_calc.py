'''
Concrete Slab Calculator

Goal: Refresh on using Python

References:
https://www.concretenetwork.com/concrete/howmuch/calculator.htm
'''

# Importing math module
import math

# Converting inches to feet
# Multiplying thickness by width by length
# Converting to cubic yards by dividing by pow(3, 3)
# Rounding to 2 decimal places
def calc_yards_cement (t, w, l):
    return round(((t/12) * w * l)/(pow(3, 3)), 2)

def print_results(t, w, l):
    print("\n\033[92m A cement slab", str(t),"inches thick,", str(w),"ft wide and", str(l),"ft long requires", calc_yards_cement(t, w, l) ,"cubic yards of cement.\033[0m\n")

print("\n========== Concrete Slab Calculator ==========\n")
thickness = None
width = None
length = None

try: 
    while thickness is None:
        try:
            thickness = float(input("- Enter the thickness of the cement in inches: "))
        except ValueError:
            print("\033[91m Invalid input. Please enter a numeric value.\033[0m\n")

    while width is None:
        try:
            width = float(input("- Enter the width of the cement in ft: "))
        except ValueError:
            print("\033[91m Invalid input. Please enter a numeric value.\033[0m\n")

    while length is None:
        try:
            length = float(input("- Enter the length of the cement in ft: "))
        except ValueError:
            print("\033[91m Invalid input. Please enter a numeric value.\033[0m\n")

    print_results(thickness, width, length)
except KeyboardInterrupt:
    print("\n\033[93m Program interrupted. Exiting gracefully.\033[0m\n")
