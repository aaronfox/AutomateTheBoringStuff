#! python3
#
#test

import re, sys, pyperclip

# NOTE: the commented out text is the strip
# function that actually substitutes in 
# for whatever is requested to strip
# def strippa(replacer=''):
#     stripRegex = re.compile(r'^\s+|\s+$')
# 
#     text = str(pyperclip.paste())
# 
#     newText = stripRegex.sub(replacer, text)
# 
#     pyperclip.copy(newText)
# 
#     if text == newText:
#         print("No changes were made to your text")
#     else:
#         print("Replaced \"" + text + "\" with \"" + newText + "\"")

def strippa(replacer=' '):
   stripRegex = re.compile(r"^" + re.escape(replacer) + r"+|" + re.escape(replacer) + r"+$")

   text = str(pyperclip.paste())

   newText = stripRegex.sub('', text)

   pyperclip.copy(newText)

   if text == newText:
       print("No changes were made to your text")
   else:
       print("Replaced \"" + text + "\" with \"" + newText + "\"")
   
if len(sys.argv) == 1:
    strippa()
else:
    strippa(sys.argv[1])
