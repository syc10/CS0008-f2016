# name       : Spencer Chen
# email      : syc10@pitt.edu
# date       : 10/28/2016
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
#
# Activity 2
#
# Notes:
#

#Define main function
def main():
# Asks user for a file name, result will be a string
    file = input('File to be read: ')
#Set inital totals to 0
    TN = 0
    TD = 0
# While loop. If string is 'q', 'quit', or empty, skips loop
#Otherwise, program will look for file with name provided by user input
    while file != 'q' and file != 'quit' and file !='':
#fh is the file object associated with the file the user requests
#This file is opened in read mode because it will not be edited
        fh = open(file,'r')
#Processes file (fh, explained below)
#Also returns PTN (partial total number of lines) and PD (partial distance run)
        PTN, PD = processFile(fh)
#Total number and distance is the total so far plus the new partial
        TN = TN + PTN
        TD = TD + PD
#Closes file because all relevant data already taken out
        fh.close()
#Prints partial total of lines and distance with the printKV function
        printKV('Partial Total # of lines',PTN)
        printKV('Partial distance run',PD)
#Asks for another file
        file = input('\nFile to be read: ')
#After user enters 'q', 'quit', or empty string, while loop ends and program goes here
    print("\nTotals")
#Prints total number of lines and distance with printKV
    printKV('Total # of lines: ', TN)
    printKV('Total distance run: ', TD)


#Define processFile function. This will take the file name and read file.
#After reading the file, it will return 2 values: # lines and

#Define processFile function. File name is passed as argument
def processFile(fh):
#Set initial partial number of lines to 0
    PTN = 0
#Set initial partial distance run to 0
    PD = 0
#for loop processes every line in file
    for line in fh:
#Add 1 to partial number of lines for each line processed
        PTN += 1
#Variable line is defined as each line of the file.
#rstrip removes newline characters at end of each line
        line = line.rstrip('\n')
#Variable temp separates names with distances
        temp = line.split(',')
#Variable distance is assigned to the distance value found in each line as a float
        distance = float(temp[1])
        PD += distance
    return PTN, PD


#Define printKV function. 2 Arguments: key and value
#Key is the string preceeding value, value is the (usually) numerical result
def printKV(key,value):
#Tests to see if the value is a string
    if isinstance(value, str):
#If value is a string, it will have 20 spaces
        fs = '20s'
#Tests to see if value is a float
    elif isinstance(value, float):
#If value is a float, 10 spaces including 3 decimal places
        fs = '10.3f'
#Tests to see if value is an integer
    elif isinstance(value, int):
#If value is an integer, 10 spaces
        fs = '10n'
#Prints key, colon, and value
    print(format(key,'25s')+": " + format(value, fs))

#Run the program
main()