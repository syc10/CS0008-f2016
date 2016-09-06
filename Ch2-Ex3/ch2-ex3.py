# name       : Spencer Chen
# email      : syc10@pitt.edu
# date       : 09/06/2016
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
#
# "Chapter 2 Exercise 3 bis" from the document titled "Chapter2.exercises" on Courseweb
#
# Notes:
#
# I hope this was submitted properly

# Ask user to input total square meters of land
# Convert value to float and assign float to variable
SqMeters = float(input("Enter total amount of land in square meters: "))
# Convert input stored in SqMeters to acres
Acres = (SqMeters/4046.8564224)
print(Acres)