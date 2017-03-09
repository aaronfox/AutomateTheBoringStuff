#! python3
#
# madLibs.py - reads in a file and allows user to play mad libs
# and then puts the result in a seperate text file

import re

# Create a Regex that searches for just the words without the punctuation
regexPartsofSpeech = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')


# Read in a file for the user to play mad libs with
readFile = open('mad_libs_sheet.txt', 'r')


# Search the file for each occurence of 
# ADJECTIVE, NOUN, ADVERB, or VERB and store each instance into a list
readFileContent = readFile.read()
partsOfSpeechList = regexPartsofSpeech.findall(readFileContent);


# Ask the user for each adjective, noun, adverb, or verb and store into the list
userResponses = []

for i in range(len(partsOfSpeechList)):
    if partsOfSpeechList[i][0] == 'A':
        userResponses.append(input("Please enter an " + partsOfSpeechList[i] + ': '))
    else:
        userResponses.append(input("Please enter a " + partsOfSpeechList[i] + ': '))


# Create a new file to write to
writeFile = open('mad_libs_sheet_result.txt', 'w')

alteredReadFileContent = readFileContent

for i in range(len(partsOfSpeechList)):
    alteredReadFileContent = alteredReadFileContent.replace(partsOfSpeechList[i], userResponses[i], 1)

writeFile.write(alteredReadFileContent)

# Don't forget to close the files
readFile.close()
writeFile.close()
