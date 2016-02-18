from lxml import etree as ET


def create_play_list():
    i = 0
    try:
        des_xml_file = 'youtubekara_playlist.xspf'
        root = ET.Element('playlist', version = "1", xmlns = "http://xspf.org/ns/0/")
        trackList = ET.SubElement(root, 'trackList')
        for line in f:
            i = i + 1
            data = line.split(';')
            title_ = unicode(data[0], encoding = 'utf-8')
            link_ = data[3]
            track = ET.SubElement(trackList, 'track')
            ET.SubElement(track, 'title').text = title_
            ET.SubElement(track, 'location').text = link_
    except Exception, e:
        er = str(e)
        print('Loi o dong %d cua file, chi tiet loi %s'%(i,er))

    tree = ET.ElementTree(root)
    tree.write(des_xml_file,encoding='utf-8',xml_declaration=True,pretty_print=True)




def main():
    create_play_list()

if __name__ == '__main__':
    f = open('youtubelist0000.txt', 'r')
    main()
    f.close()