#! python3
#
# removeSensitive.py - removes sensitive information such as social security numbers or credit card numbers

import re, pyperclip

# sensitiveRegex 
sensitiveRegex = re.compile(r'''(
        (\d{11,16})                # looks for credit card numbers
        |(\d{3}(-)?\d{2}(-)?\d{4})   # looks for social security numbers
         )''', re.VERBOSE)

# TODO paste test from clipboard and have regex censor it

text = str(pyperclip.paste())

print(sensitiveRegex.sub('SENSITIVE INFO',text))

