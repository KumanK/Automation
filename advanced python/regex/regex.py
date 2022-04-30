import re

# stri = 'hllp csdc900 cnks 898 8d9ddj k29 asjk_77 scc--3278 aspkdkj83129 sskd---333'
# stri = 'clock mock heep jeep cheep mode code shock deep'
# stri = 'GeeksforGeeks'

# expr = re.compile()
# print re.findall("\d{3,}",stri)
# print re.findall("[aA-zZ]{3,}",stri)
# print re.findall("as[j|p]",stri)
# print re.findall("[a-z]{2,}ck",stri)
# print re.findall("[aA-zZ]+eep",stri) # every word ending with eep
# print re.findall("c[aA-zZ]+",stri) # every word starting with c
# stri = ' sggsforgeeks ... hsjsjcks .... sjijs scdop'
# print re.findall(" s\w{1,}s ",stri) # every word starting with s & ending with s
# stri = 'sggsforgeeks'
# print re.findall("^s",stri) # every word starting with s & ending with s
# print re.findall("s$",stri) # every word starting with s & ending with s
# print re.findall("",stri)
# stri = '666kk888 4kk4 mmk888 ufsdjfkksiduhfi'
# print re.findall("[aA0-zZ9]{1,}kk[aA0-zZ9]{1,}",stri)
# stri = 'wsc lsdj 11:08:23 c,ccocj csc 90:07:33 .......5:07:44 ,sdcsdchc.......'
# parse = re.findall("\d{1,}:[0-9]{1,2}:[0-9]{1,4}",stri)
# print parse
# stri = 'sjdoc 192.168.0.2,,sdjcic 10.231.129.20 ......ccsdhi 900.129.229.45 acjsc'
# parse = re.findall("[1-2]{1,3}.\d{1,3}.\d{1,3}.\d{1,3}",stri)
# print parse

# stri = 'startiiiiiiiicnd'
# parse = re.findall("\Astart|end\Z",stri)
# print parse

# stri = 'code mode lode kode'
# parse = re.findall("[cm]ode",stri) # either c or m
# print parse


# stri = '233.244.22.34'
# stri = '233.333.322.3220'
# stri = '233'
# print re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',stri)
# print re.findall(r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',stri)
# print re.findall(r'[01]?[0-9][0-9]?',stri)

# stri = '4253625879615786'
# stri = '4253-6258-7961-5786'
# stri = '44253-6258-7961-578'
# stri = '4253 6258 7961-5786'
# stri = '6253625879615786'
# stri = '8165863385679329'
# stri = '8165863385679329'
# L = len(stri)
# print(re.findall(r'(^[4|5|6])([\d]{3}-[\d]{4}-[\d]{4}-[\d]{4}|\d{15})',stri))
# print(re.findall(r'[a-zA-Z0-9 \-_\\.]{1,}@\w{1,}.[a-zA-Z]{1,3}','dexter@hotmail.com'))
# print(re.findall(r'[a-zA-Z0-9\-_\.]{1,}@\w{1,}.[a-zA-Z]{1,3}','dexte44r@@hotmail.com'))
# print(re.findall(r'^[4|5|6\][0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}',stri))
# print(re.findall(r'([a-zA-Z0-9\-_.]+'
#                  r'@\w+'
#                  r'\.[a-zA-Z]{1,3})','.vin@gmail.com'))

# print(re.findall(r'[1-9]{1}[0-9]{5}','123456'))
# print(re.findall(r'[1-9]{1}[0-9]{5}','899099'))
# print(re.findall(r'(\d)(?:\d)(\1)+','8790599'))
# print(dir(object))