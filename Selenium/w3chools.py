'''
Usage:  getMeLink ('XXXXXX')
XXXXXX = any item name from defined flows in w3Schools.json
'''

from base_classes import redirectTo
from base_classes import findPath
from base_classes import getDriver


# O.redirect("Color Names")
# O.redirect("DeepPink")

d=findPath("w3Schools.json")
Link= d.getMeLink('DeepPink')
O=redirectTo("https://www.w3schools.com")
for ele in Link[1:]:
    O.redirect(ele.decode())


