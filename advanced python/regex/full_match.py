import re
text = 'lovely loudly'

print(re.fullmatch('l....y',text))
print(re.findall('l[a-z]{4}y',text))