import re
text = "Duis info@geeksforgeeks.com convallis. Parturient montes nascetur ridiculus mus \
geeksforgeeks@rocks.xyz mauris. Odio eu feugiat pre@rsos_tium.index nibh ipsum consequat love@gfg.in \
pretium aenean pharetra magna ac placerat. Vitae justo eget magna fermentum iaculis eu non."

# stri = 'ankitrai326@gmail.com'
# stri = 'riono23@indi.com kkj28kumanj@gmail.com schc.sjdj.com'
# print re.findall(r'\w{1,}@[aA-zZ]{1,}.[aA-zZ]{1,}',stri)
# stri = 'ankitrai326gmail.com'
# stri = 'https://www.geeksforgeeks.org/'
# stri = 'https://www. geeksforgeeks.org/'
# print (re.findall(r'http[s]://www.\w{1,}.[aA-zZ]{1,}',stri))
# print(re.findall(r'[aA0-zZ9]{1,}@[aA0-zZ9]{1,}.[aA-zZ]{1,5}',text))

print(re.findall(r'[aA0-zZ9,\-_]{1,}@[aA0-zZ9]{1,}.[aA-zZ]{1,3}',
                 'ha@git@int.cz'))