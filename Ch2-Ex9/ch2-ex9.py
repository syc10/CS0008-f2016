# Needs work
# ask pocket number (1-36), displays a number

# First thing to do: ask user for an input
# Assign it to a variable
# 2 checks: Make sure it is an INT and then make sure it's in the range


# Ask user for input
number = input("Please enter number between 0 and 36 ")
# Make sure number is int and between 0 and 36, inclusive
number = int(number)
#
if number < 0 or number > 36:
    print("That isn't a valid number")

if number == 0:
    color = "Green"
elif (number >= 1 and number <= 10)\
        or \
        (number >= 19 and number <= 26):
#odd numbers red, even numbers black
    if number % 2 == 0:
        color = "Black"
    else:
        color = "Red"
elif (number >= 11 and number <= 18):
    if number % 2 == 0:
        color = "Red"
    else:
        color = "Black"





print(color)