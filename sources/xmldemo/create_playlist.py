from lxml import etree as ET
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree
from xml.dom import minidom
import io


"""
using lxml
"""
def create_play_list():
    i = 0
    des_xml_file = 'youtubekara_playlist.xspf'
    root = ET.Element('playlist', version = "1", xmlns = "http://xspf.org/ns/0/")
    trackList = ET.SubElement(root, 'trackList')
    try:
        for line in f:
            # i = i + 1
            # if i == 100:
            #     break
            data = line.split(';')
            title_ = unicode(data[0], encoding = 'utf-8')
            link_ = unicode(data[3], encoding = 'utf-8').replace('\n','')
            img_url = 'http://img.youtube.com/vi/' + link_.split("?v=")[1] + '/2.jpg'
            track = ET.SubElement(trackList, 'track')
            ET.SubElement(track, 'location').text = link_
            ET.SubElement(track, 'title').text = title_
            ET.SubElement(track, 'image').text = img_url
    except Exception, e:
        er = str(e)
        print('Loi o dong %d cua file, chi tiet loi %s'%(i,er))

    tree = ET.ElementTree(root)
    tree.write(des_xml_file,encoding='utf-8',xml_declaration=True,pretty_print=True)


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = etree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

"""
using xml.etree
"""
def create_play_list2():
    i = 0
    des_xml_file = 'youtubekara_playlist.xspf'
    root = Element('playlist')
    root.set('version', '1')
    root.set('xmlns', 'http://xspf.org/ns/0/')
    trackList = Element('trackList')
    root.append(trackList)
    try:
        for line in f:
            i = i + 1
            if i == 100:
                break
            data = line.split(';')
            title_ = unicode(data[0], encoding = 'utf-8')
            link_ = unicode(data[3], encoding = 'utf-8').replace('\n', '')
            track = Element('track')
            trackList.append(track)
            title = Element('title')
            title.text = title_
            track.append(title)
            location = Element('location')
            location.text = link_
            track.append(location)
            # ET.SubElement(track, 'location').text = link_
            # ET.SubElement(track, 'title').text = title_
    except Exception, e:
        er = str(e)
        print('Loi o dong %d cua file, chi tiet loi %s'%(i,er))

    # tree = ET.ElementTree(root)
    # tree.write(des_xml_file,encoding='utf-8',xml_declaration=True,pretty_print=True)
    f2 = io.open(des_xml_file, 'w', encoding = 'utf-8')
    f2.write(prettify(root))
    f2.close()


def main():
    create_play_list()

if __name__ == '__main__':
    f = open('youtubelist0000.txt', 'r')
    main()
    f.close()