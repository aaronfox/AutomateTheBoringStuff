#! python3
#
# fillingInTheGaps.py - finds all files with a given prefix in a folder
# and located any gaps in the numbering
# NOTE: this is currently only functional for numbers up to 9, if
# you're naming a file the same thing over 9 times... :-/

import re, os, glob, shutil

# entire desired prefix to find here
prefixToFind = "txt"

preRegex = re.compile(r'^(' + re.escape(prefixToFind) + r')(.*?)(\d+)(.*)')

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
    numChangeBool = 0
    initialRun = 0

    for files in glob.glob('*.txt'):
        fileToExamine = preRegex.findall(files)
        if fileToExamine:
            if numChangeBool == 0:
                if initialRun == 0:
                    currentNumber = int(fileToExamine[0][2])
                    initialRun = 1
                    continue
                # see if there is a nonsequential file
                if currentNumber + 1 is not int(fileToExamine[0][2]):
                    # rename all files to be in sequence
                    print('00' + str(int(fileToExamine[0][2])-1) + ' is the missing culprit')

                    print('BOOYAH')
                    numChangeBool = 1
            if numChangeBool == 1:
                oldFileName = fileToExamine[0][0] + fileToExamine[0][1] + fileToExamine[0][2] + fileToExamine[0][3]
                newFileName =  fileToExamine[0][0] + fileToExamine[0][1] + '00' + str(int(fileToExamine[0][2]) - 1) + fileToExamine[0][3]


                print('Moving ' + oldFileName + ' to ' + newFileName)
                shutil.move(os.path.abspath(os.path.join('.', oldFileName)), os.path.abspath(os.path.join('.', newFileName)))
            currentNumber = int(fileToExamine[0][2])

print(str(findTheGap()))
