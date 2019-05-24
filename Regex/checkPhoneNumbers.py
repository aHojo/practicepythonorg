""" 
This will get replaced with Regex
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))
"""

import re

# Passing a string value representing your regular expression to re.compile() returns a Regex pattern object (or simply, a Regex object).

#phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Adding parentheses will create groups in the regex: (\d\d\d)-(\d\d\d-\d\d\d\d).
""" passing the integer 1 or 2 to the group() match object method, you can grab different parts of the matched text. Passing 0 or nothing to the group() method will return the entire matched text. """
#phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
# print(mo.group()) # 415-555-9999

# If we want to match parenthesis have to escape it.
# phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is (415)-555-4242.')
# print('Phone number found: ' + mo.group())
# print('Phone number found: ' + mo.group(1))
# print('Phone number found: ' + mo.group(2))

#  retrieve all the groups at once, use the groups() method
# print(f"Both groups {mo.groups()}")  # ('415', '555-4242')
# areaCode, mainNumber = mo.groups()
# print(areaCode)
# print(mainNumber)

# The ? character flags the group that precedes it as an optional part of the pattern.
# This matches on area code or not
# phoneNumRegex = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# mo = phoneNumRegex.search('My number is 555-4242.')
# print('Phone number found: ' + mo.group())
""" 
A Regex object’s search() method searches the string it is passed for any matches to the regex. The search() method will return None if the regex pat- tern is not found in the string. If the pattern is found, the search() method returns a Match object. Match objects have a group() method that will return the actual matched text from the searched string. 
"""
""" In addition to the search() method, Regex objects also have a findall() method. While search() will return a Match object of the first matched text in the searched string, the findall() method will return the strings of every match in the searched string.  """

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
# print(mo.group())  # 415-555-9999

# On the other hand, findall() will not return a Match object but a list of strings—as long as there are no groups in the regular expression.

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
# ['415-555-9999', '212-555-0000']
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

# If there are groups in the regular expression, then findall() will return a list of tuples.
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))


"""
Character Classes
\d Any number 0 - 9
\D Any character that is not a numeric digit from 0-9
\w Any letter numeric digit, or the underscore character
\W Is not the above
\s Any space tab or newline char
\S Anything that is not empty space
"""

"""
MAKING YOUR OWN CHARACTER CLASS
"""
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowels = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(vowels)  # ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

""" 
character class [a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers.
Note that inside the square brackets, the normal regular expression symbols are not interpreted as such. This means you do not need to escape the ., *, ?, or () characters with a preceding backslash. For example, the character class [0-5.] will match digits 0 to 5 and a period. You do not need to write it as [0-5\.].
By placing a caret character (^) just after the character class’s opening bracket, you can make a negative character class. A negative character class will match all the characters that are not in the character class. 
"""
consonantRegex = re.compile(r'[^aeiouAEIOU]')
notVowels = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
# ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
print(notVowels)

""" 
caret symbol (^) - Match beginning of line
dollar sign ($)  - Match End of Line
You can use the ^ and $ together to indicate that the entire string must match the regex
"""
beginsWithHello = re.compile(r'^Hello')
match = beginsWithHello.search("Hello World!")
print(match)  # <re.Match object; span=(0, 5), match='Hello'>

endsWithNumber = re.compile(r'\d$')
otherMatch = endsWithNumber.search('Your number is 52')
print(otherMatch)  # <re.Match object; span=(16, 17), match='2'>

wholeStringIsNum = re.compile(r'^\d+$')
numString = wholeStringIsNum.search('987524973953')
print(numString.group())

""" 
The . (or dot) character in a regular expression is called a wildcard and will match any character except for a newline.
"""

atRegex = re.compile(r'.at')
atRegex1 = atRegex.findall('The cat in the hat sat on the flat mat.')
# ['cat', 'hat', 'sat', 'lat', 'mat']
print(atRegex1)

"""
.* - Match anything
Greedy vs Non Greedy
"""

nongreedyRegex = re.compile(r'<.*?>')

mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo.group()
'<To serve man>'

greedyRegex = re.compile(r'<.*>')

mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group()
# '<To serve man> for dinner.>'

""" 
By passing re.DOTALL as the second argument to re.compile(), you can make the dot character match all characters, including the newline character.
"""


noNewlineRegex = re.compile('.*')
noNewlineRegex.search(
    'Serve the public trust.\nProtect the innocent. \nUphold the law.').group()
# Serve the public trust.'
newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search(
    'Serve the public trust.\nProtect the innocent. \nUphold the law.').group()
# Serve the public trust.\nProtect the innocent.\nUphold the law.'

""" 
To make your regex case-insen- sitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile()
"""
robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()
# 'RoboCop'
robocop.search('ROBOCOP protects the innocent.').group()
# 'ROBOCOP'
robocop.search(
    'Al, why does your programming book talk about robocop so much?').group()
# 'robocop'

""" 
Substituting Strings with the sub() method
The sub() method for Regex objects is passed two arguments. The first argument is a string to replace any matches. The second is the string for the regular expression. The sub() method returns a string with the substitutions applied.
"""

namesRegex = re.compile(r'Agent \w+')
namesRegex.sub(
    'CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
# 'CENSORED gave the secret documents to CENSORED.'

"""  
metimes you may need to use the matched text itself as part of the substitution. In the first argument to sub(), you can type \1, \2, \3, and so on, to mean “Enter the text of group 1, 2, 3, and so on, in the substitution.”
"""
agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(
    r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
# A**** told C**** that E**** knew B**** was a double agent.'


"""  
ignore whitespace and comments inside the regular expression string. This “verbose mode” can be enabled by passing the variable re.VERBOSE as the second argument to re.compile().
Now instead of a hard-to-read regular expression like this:
            phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}
            (\s*(ext|x|ext.)\s*\d{2,5})?)')

you can spread the regular expression over multiple lines with comments like this:
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
Note how the previous example uses the triple-quote syntax (''') to create a multiline string so that you can spread the regular expression defi- nition over many lines, making it much more legible.
"""

""" 
You can get around this limitation by combining the re.IGNORECASE, re.DOTALL, and re.VERBOSE variables using the pipe character (|), which in this context is known as the bitwise or operator.
"""

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
