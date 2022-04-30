import re
print(re.findall(r'(?i)\blog\b','log of analog. LOg of a watchlog')) #matches full word 'log'
print(re.findall(r'\w+','log-of analog')) #matches full word 'log'

