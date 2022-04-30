import re
s = 'I mdsdi sdcjld sdl jsdl, dsjod'

print(re.findall(r'\w[^\s]*',s))