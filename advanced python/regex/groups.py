import re

pattern = r'\d+'
pattern2 = r'\d+(?:,\d{3})?:*'
print(re.findall(pattern,'123'))
print(re.findall(pattern2,'123,345'))