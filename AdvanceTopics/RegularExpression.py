# It is used to find patterns in strings

import  re

pattern=["this","that"]

text='this is the passage which contain this only not the other pattern'

for i in pattern:
    if re.search(i,text):
        print('Match found')
    else:
        print('Match not found')

"""
Module Regular Expressions(RE) specifies a set of strings(pattern) that matches it.
To understand the RE analogy, MetaCharacters are useful, important and will be used in functions of module re.
There are a total of 14 metacharacters and will be discussed as they follow into functions:
\   Used to drop the special meaning of character
    following it (discussed below)
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One ore more occurrences
{}  Indicate number of occurrences of a preceding RE 
    to match.
()  Enclose a group of REs

"""

# Module Regular Expression is imported using __import__().
import re

# compile() creates regular expression character class [a-e],
# which is equivalent to [abcde].
# class [abcde] will match with string with 'a', 'b', 'c', 'd', 'e'.
p = re.compile('[a-e]')

# findall() searches for the Regular Expression and return a list upon finding
print(p.findall("Aye, said Mr. Gibenson Stark"))