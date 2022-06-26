import re

str_raw = "Blah bla  h Blaaaaaah,  ,ahahha 545463 lol  . hghhgh, kwa kwa Kwa"

normalized_space = (' '.join(str_raw.split())).replace(',', '.')


def uppercase(matchobj):
    return matchobj.group(0).upper()


def capitalize(s):
    return re.sub('^([a-z])|[\.|\?|\!]\s*([a-z])|\s+([a-z])(?=\.)', uppercase, s)


formated = capitalize(normalized_space)
print(formated)

# CHECK string methods
# Regex python




