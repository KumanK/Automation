import re

# expr = r'a' # case -sensitive
expr = r'(?i)A' # case-insensitive

o = re.finditer(expr,'a text book of a mighty RAju')
print(o.__next__().group())
print(o.__next__().group())
print(o.__next__().group())
try:
    print(o.__next__().group())
except StopIteration:
    print('End of string')