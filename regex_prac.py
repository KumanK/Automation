import re
# regex = r"([a-zA-Z]+) (\d+)"
# regex = r"h\dn\d"
# regex = r"\d{3}[a-z]{3}"
# regex = r"\d{3}[A-Z]{2}"
# regex = r"\d+"
# regex = r"7\W+9"
# regex = r"7\w+9"
regex = r"\w+.py"
# match = re.findall(regex, "I was born on June 555. Kuman 344 jalsdd daldl")
# match = re.findall(regex, "I was born on June KKKKK 555JJ. L jj8888 Jnme JJLL ll000ee 909fff Kuman 344 JHeE jalsdd daldl h8n8 ,,,,%6%6")
match = re.findall(regex, "I was born on 798H djsd.120380 11-07-1991 ...323-323.dad 44%%%$$ "
                          "9090)))((( uuuhdih llolol 9d0dmmm 9d0wdbjwhd 7&&9 9090 7MM9 7&%$#(9 7dadk9 723idheu9 90_di.py"
                          "popcas_csc.py ....hasici_909_.py")

print match