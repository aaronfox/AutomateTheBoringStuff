#! python3
#
# isWebsite.py - Searches text copied from clipboad and copies any websites found in 
# that text into the clipboard

import re, pyperclip

# websiteRegex
websiteRegex = re.compile(r'''(
    (http(s)?://)           # protocol to use
    (www\.)?(.)+            # also looks for www.
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in websiteRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    websites = '\n'.join(matches)
    pyperclip.copy(websites)
    print('Copied to clipboard: ')
    print(websites)
else:
    print('No websites were found :(')

