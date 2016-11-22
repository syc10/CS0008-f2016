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
#
#
#
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
#Initializes number of input files, total number of lines read, total distance run to 0
    numfiles = 0
    lines = 0
    td = 0
#Can process any number of data files. In this case, it processes 3 because 3 files are listed in Master
    for line in MIF:
#Finds name of file, strips '\n'
        datafile = line.rstrip('\n')
#Uses processFile function to return ????????????????
        numlines, pd = processFile(datafile)
#Adds 1 to number of input files per file
        numfiles += 1
#Adds total number of lines obtained from data file
        lines += numlines
#Adds partial distances to total distance
        td += pd
#Prints results
    print('Number of Input files read   : ' + str(numfiles))
    print('Total number of lines read   : ' + str(lines))
    print('\nTotal distance run           : ' + str(td))

#This function processes the individual data files
def processFile(datafile):
    dict = {}
    file = open(datafile, 'r')
    numlines = 0
    pd = 0
    for line in file:
        numlines += 1
        name = line.rstrip('\n')
        temp = line.split(',')
        readname = temp[0]
        readnum = temp[1]
        pd += float(readnum)
        if readname in dict:
            dict[readname] += float(readnum)
        else:
            dict[readname] = float(temp[1])
    file.close()
#    print(dict)




    return numlines, pd


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