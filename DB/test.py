import xml.etree.ElementTree as ET

tree = ET.parse("test.xml")
root = tree.getroot()
pro = tree.find('InstallPath')
print(pro.text)
pro = tree.find('Version')
print(pro.text)
# bdta = root[0].text.encode('utf8')
# bdta = root[1].text.encode('utf8')
# print(''.join(bdta.decode('utf8')))

