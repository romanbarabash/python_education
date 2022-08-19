import re

'''
.        Matches any single character
\        Escapes one of the meta characters to treat it as a regular character
[...]    Matches a single character or a range that is contained within brackets. Order does not matter but without brackets order does matter
+        Matches the preeceding element one or more times
?        Matches the preeceding element zero or one time
*        Matches the preeceding element zero or more times
{m,n}    Matches the preeceding element at least m and not more than n times
^        Matches the beginning of a line or string
$        Matches the end of a line or string
[^...]   Matches a single character or a range that is not contained within the brackets
?:...|..."Or" operator
()       Matches an optional expression
'''

with open('ipis.txt', 'r') as file:
    content = file.read()

pattern = re.compile('[0-9]{3}\.[0-9]{3}\.[0-9]{3}\.[0-9]{3}')  # find all ips with 3 digits in it
matches = pattern.findall(content)
print(matches)
