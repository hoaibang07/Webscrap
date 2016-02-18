from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree
from xml.dom import minidom
import io

"""
using xml.etree.ElementTree
"""


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = etree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

root = Element('person')
tree = ElementTree(root)
name = Element('name')
root.append(name)
name.text = 'Julie'
root.set('id', '123')
# print etree.tostring(root)
print(prettify(root))
tree.write(open('person.xml', 'w'))
f2 = io.open('person2.xml', 'w', encoding = 'utf-8')
f2.write(prettify(root))