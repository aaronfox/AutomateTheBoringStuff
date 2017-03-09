#! python3
#
# regexSearch.py - searches all txt files in a folder and prints out all lines that match the desired regex

import re, os

# change to the desired directory to search txt files
os.chdir('randomQuizzes')

regexSearch = re.compile(r'Kentucky')

for files in os.listdir(os.getcwd()):
    readFile = open(files, 'r')
    readFileList= readFile.readlines()

    for i in readFileList:
        regMatchObj = regexSearch.search(i)

        if regMatchObj:
            print(i)
