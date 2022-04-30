import re

# same words repeated by some specifier
# patt = r'(?P<word>\w+)\s+(?P=word)'
patt2 = r'(?P<word>\b\w+\b)-(?P=word)'

# o = re.findall(patt,'hello csnkc ko ko ro rro ro')
o = re.findall(patt2,'hello csnkc kom-kom rcasc word-ord')
print(o)
