#!/usr/bin/python2.7

from lxml import etree as ET
import io
import sys

"""
    The program use lxml module for write xml
"""

def head_xml(root,headers):
    """
        Write header of xml with format:
        <head>
            <title>title</title>
            <description>description</description>
            <author>author</author>

        </head>
    """
    _title = headers[0]
    _description = headers[1]
    _author = headers[2]
    head = ET.SubElement(root,'head')
    title = ET.SubElement(head,'title').text = _title
    description = ET.SubElement(head,'description').text = _description
    author = ET.SubElement(head,'author').text = _author
def content_xml(root,source_file_name):
    """
        Write content fo xml file with format:
        <content>
            <pair id = 1>
            <sentence lang='cn'type="original"></sentence>
            <sentence lang=vi type="translate"></sentence>
            ...
            </pair>
        </content>
    """
    content = ET.SubElement(root,'content')
    i = 1
    f = io.open(source_file_name,'r',encoding='utf-8')
    #flag for headers
    flag_headers = True
    for line in f:
        if not flag_headers:
            words = line.strip().split('|')
            #minus 5 line headers
            pair = ET.SubElement(content,'pair',id='%s'%(i-5))
            ET.SubElement(pair,'sentence',lang='cn',type='original').text = words[0]
            if len(words[1:]) == 1:
                j = 1
                ET.SubElement(pair,'sentence',lang='vn',type='translate',version="%s"%j).text = words[1]
            else:
                for j in range(1,len(words)):
                    ET.SubElement(pair,'sentence',lang='vn',type='translate',version="%s"%j).text = words[j]
        else:
            if line.strip() == '--End-header--':
                flag_headers = False
        i = i + 1
    f.close()
def read_header_file(source_file_name):
    headers = []
    f = io.open(source_file_name,'r',encoding='utf-8')
    for line in f:
        if line.strip() == "--End-header--":
            break
        if not line.strip() == "--Begin-header--":
            headers.append(line.strip())

    return headers
def convert(source_file_name,destination_xm_file,headers):
    root = ET.Element("doc")
    head_xml(root,headers)
    content_xml(root,source_file_name)
    tree = ET.ElementTree(root)
    tree.write(destination_xm_file,encoding='utf-8',xml_declaration=True,pretty_print=True)

def main():
    args = sys.argv[1:]
    if not args:
        print "[USAGE] convert2xml.py source_file_name destination_xm_file [--line]"
        sys.exit(1)
    if len(args) == 2:
        source_file = args[0]
        destination_file = args[1]
        headers = read_header_file(args[0])
        convert(source_file,destination_file,headers)
if __name__ == '__main__':
    main()
