import re

COLORS_PATH = './_colors.less'
CODE_PATH = './_broccoli.less'

# This function does find and replace in a file based on the key-value
# pairs in a dictionary
def findAndReplace(string, dictionary):
    # Sort keys by length, in reverse order
    # Do this to replace longest strings first
    for item in sorted(dictionary.keys(), key = len, reverse = True):
        string = re.sub(item, dictionary[item], string)
    return string

# Make a dictionary from the color constants file with the hex as keys
# {hex1:name1, hex2:name2, ...}
colorsFile = open(COLORS_PATH, 'r')
colors = colorsFile.read()
colorsRegex = '(@.*?):\s*(#.*?);'
colorsList = re.findall(colorsRegex, colors)
colorsDict = {}
for color in colorsList:
    colorsDict[color[1]]=color[0]

# Read the file you want to edit into memory
codeFile = open(CODE_PATH, 'r+', errors='replace')
code = codeFile.read()

# Replace the hex with less variables
newCode = findAndReplace(code, colorsDict)

# Overwrite the file
codeFile.seek(0)
codeFile.truncate()
codeFile.write(newCode)
codeFile.close()

print('All Done!')
print('Hex values replaced with .less variables in '+CODE_PATH)
