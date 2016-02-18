from lxml import etree as ET


root = ET.Element("person", id = '123')
ET.SubElement(root, 'name').text = 'Julie'
print(ET.tostring(root, encoding='utf-8', xml_declaration=True, pretty_print=True))
print('cc')
des_xml_file = 'person23.xml'
tree = ET.ElementTree(root)
tree.write(des_xml_file,encoding='utf-8',xml_declaration=True,pretty_print=True)

