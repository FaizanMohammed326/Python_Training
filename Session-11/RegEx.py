"""
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.

Python has a built-in package called re, which can be used to work with Regular Expressions.

Metacharacters in regex:
[]	A set of characters
\	Signals a special sequence (can also be used
    to escape special characters)
.	Any character (except newline character)
^	Starts with
$	Ends with
*	Zero or more occurrences
+	One or more occurrences
?	Zero or one occurrences
{}	Exactly the specified number of occurrences
|	Either or

Special Sequences
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"
\D	Returns a match where the string DOES NOT contain digits	"\D"
\s	Returns a match where the string contains a white space character	"\s"
\S	Returns a match where the string DOES NOT contain a white space character

Functions in Regex
1.Search()
    Returns a Match object if there is a match anywhere in the string
"""
import re

txt = "My Name is Faizan and I stay in India"
x = re.search("Faizan", txt)
if x:
    print("We have a match")
else:
    print("No match")

# If no matches are found, the value None is returned

x = re.search("Mohammed", txt)
print(x)
print('\n')

"""
2. findall():
    The findall() function returns a list containing all matches.
"""

x = re.findall("i", txt)
print(x)
print('\n')

"""
split()
    The split() function returns a list where the string has been split at each match:
"""

x = re.split("i", txt)
print(x)

y = re.split("i", txt, 2)
print(y)
print('\n')

"""
sub()  :
    The sub() function replaces the matches with the text of your choice:
"""

x = re.sub("a", "e", txt)
print(x)

y = re.sub("a", "e", txt, 2)
print(y)
print('\n')
