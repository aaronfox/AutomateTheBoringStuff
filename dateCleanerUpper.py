#! python3
#
# dateCleanerUpper.py - finds dates from the clipboard and puts them in a consistent format then copies to clipboard

import re, pyperclip

dateRegex = re.compile(r'''(
       (\d+)
       [-/\\.]
       (\d+)
       [-/\\.]
       (\d+)      

        )''', re.VERBOSE)

# Find dates in clipboard text
text = str(pyperclip.paste())

matches = []

for groups in dateRegex.findall(text):
    group1 = groups[1]
    group2 = groups[2]
    if len(groups[1]) < 2:
       group1 = str('0') + groups[1]
    if len(groups[2]) < 2:
       group2 = str('0') + groups[2]

    date = '/'.join([group1, group2, groups[3]])
    matches.append(date)

# copy results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No dates were found')
