#! python3
#
# fillingInTheGaps.py - finds all files with a given prefix in a folder
# and located any gaps in the numbering

import re, os, glob

# entire desired prefix to find here
prefixToFind = "txt"

preRegex = re.compile(r'^(' + re.escape(prefixToFind) + r').*?(\d+)')

directoryToSearch = os.path.abspath('.\\textFiles')    

os.chdir(directoryToSearch)

# you can use this method if you want to find the gaps for specific types
# of files by inserting this function into.. TODO
# def countNumFilesWithExt(extension):
#     count = 0
#     list_dir = os.listdir(os.path.abspath('.'))
#     for files in list_dir:
#         if files.endswith('.txt'):
#             count = count + 1
#     return count

# this functions assumes files are automatically in alphabetical order
def findTheGap():

    currentNumber = 0
    initialRun = 0

    for files in glob.glob('*.txt'):
        fileToExamine = preRegex.findall(files)
        if fileToExamine:
            if initialRun == 0:
                currentNumber = int(fileToExamine[0][1])
                initialRun = 1
                continue
            # see if there is a nonsequential file
            if currentNumber + 1 is not int(fileToExamine[0][1]):
                # rename all files to be in sequence
                print('00' + str(int(fileToExamine[0][1])-1) + ' is the missing culprit')

                print('BOOYAH')
                return int(fileToExamine[0][1])
            currentNumber = int(fileToExamine[0][1])

print(str(findTheGap()))
