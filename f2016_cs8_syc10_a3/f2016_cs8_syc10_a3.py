# name       : Spencer Chen
# email      : syc10@pitt.edu
# date       : 11/18/2016
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Assignment #3
#
# Notes:
# MN: please respect indentation with commetns too
#
#
#1. Read master input list file (txt). Obtain names of files
#
#2. Extract name and distance
#
#3. Compute the following
#   Number of files read
#   Total number of lines read
#   Total distance run (sum of all distances loaded from provided files)
#   Total distance run for each individual
#   Individual maximum distance run and by who
#   Individual minimum distance run and by who
#   Note who appears more than once, and how many times they appear
#   Total number of participants
#


#This function opens the Master input file, then opens the files that are in the Master. It then processes a lot of the data
def openFile(MIF):
    #Creates dictionary for everything
    dictionary = {}
    #Initializes number of input files, total number of lines read, total distance run to 0
    numfiles = 0
    lines = 0
    td = 0
    #Can process any number of data files. In this case, it processes 3 because 3 files are listed in Master
    for line in MIF:
        #Finds name of file, strips '\n'
        datafile = line.rstrip('\n')
        #Uses processFile function to return ????????????????
        numlines, pd, pdict = processFile(datafile)
        #Adds 1 to number of input files per file
        numfiles += 1
        #Adds total number of lines obtained from data file
        lines += numlines
        #Adds partial distances to total distance
        td += pd
        #Compiles master dictionary with every name
        dictionary.update(pdict)
    #Prints results
    print('Number of Input files read   : ' + str(numfiles))
    print('Total number of lines read   : ' + str(lines))
    print('\nTotal distance run           : ' + str(td))
    print('\nmax distance run             : ' + str(dictionary.get(max(dictionary, key=dictionary.get))))
    print('  by participant             : ' + str(max(dictionary, key=dictionary.get)))
    print('\nmin distance run             : ' + str(dictionary.get(min(dictionary, key=dictionary.get))))
    print('  by participant             : ' + str(min (dictionary, key=dictionary.get)))
    print('\nTotal number of participants : ' + str(len(dictionary)))
    print('Number of participants\n with multiple records       : ')

#This function processes the individual data files
def processFile(datafile):
    #Creates an empty dictionary for each file
    dict = {}
    list1 = []
    #Opens the data file listed in master
    file = open(datafile, 'r')
    #Initializes number of lines and partial distance to 0
    numlines = 0
    pd = 0
    #Goes through each line with for loop
    for line in file:
        # MN: we need to filter out the files headers: name,distance\n
        #     I check if the word "distance" is in the string, and if it is, we skip the line
        if 'distance' in line:
            continue
        #Adds 1 to number of lines for each line processed
        numlines += 1
        #Strips '\n' off of each line and splits name from distance
        # MN: with this assignment you are stripping \n and assign the whole line to name
        #     that you do not use at all.
        #name = line.rstrip('\n')
        # MN: and here you are splitting at the comma the line as you read it from the file
        #     this means that the second element in temp still has \n appended
        #temp = line.split(',')
        # MN: here is the correct statement
        temp = line.rstrip('\n').split(',')
        # MN: if you want to divide it on 2 rows
        # temp = line.rstrip('\n')
        # temp = temp.split('\n')
        #Assigns first part to readname
        readname = temp[0]
        #Assigns second part to readnum
        readnum = temp[1]
        #Adds all distances together
        # MN: this statement fails because you did not filter out the files headers (name,distance)
        #     No it works with the conditional filtering of the headers
        pd += float(readnum)
        #If name already exists, adds distance
        if readname in dict:
            dict[readname] += float(readnum)
        #If name does not exist, make a new dictionary entry
        else:
            dict[readname] = float(temp[1])
            list1.append([readname, 1, readnum])
    #Close file
    file.close()
    #Return useful tidbits of information
    return numlines, pd, dict


#Main function
def main():
    #Asks user for desired Master input list
    master = input('Master input file name: ')
    #Open the master
    MIF = open(master, 'r')
    #Process master
    openFile(MIF)
    #Close the master
    MIF.close()

#Run the program
main()
