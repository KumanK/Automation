# Scenario:
#
# Must start with http or https or ftp followed by ://
# Must match a valid domain name
# Could contain a port specification (http://www.sitepoint.com:80)
# Could contain digit, letter, dots, hyphens, forward slashes, multiple times

import re
# stri = 'http://www.sitepoint0023.com:80'
# stri = 'http://www.sitepoint0023.com:8090'
# stri = 'http://www.9009..//sitepoint0023.com:8090'
# stri = 'http://www.siteSSAp32.com:80'
# stri = 'http://www.si)teSSAp32.com:80'
# stri = 'http&//www.sitepoint.com:80'
# stri = 'http://www(sitepoint.com:80'
stri = 'http://www.sitepoint_93293.com:80'

O =re.findall(r'^(http|https|ftp)(://[w]{3}\.[a-zA-Z0-9_+\/%&*><]+\.)(com|in|org)(:[0-9]+)',stri)
print(O)
# print(stri[O.start():O.end()])