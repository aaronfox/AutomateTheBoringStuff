#! python3
#
# strongPasswordsDetection.py - detects if a password is strong or not
# Here, strong is defined as a password that is at least
# 8 characters long, contains at least one capital letter, one lowercase letter
# and at least one number
#
# From the Strong Password Detection prompt of Automate the Boring Stuff with Python
# by Al Sweigart

import re, pyperclip

passRegex = re.compile(r'''
    ^(?=.*[A-Z])                # Lookahead to ensure there is at least one capital letter
    (?=.*[a-z])                 # Lookahead to ensure there is at least one capital letter
    (?=.*\d)                    # Lookahead to ensure that there is at least one numeric digit
    .+\w{8,}$                   # Ensure that the password is at least at characters long
    ''', re.VERBOSE)

text = str(pyperclip.paste())

mo = passRegex.search(text)

if(mo):
    print('That password is super strong, my dude.')
else:
    print('That password certainly could use some work. Strive for a strong password.')
