import re
import io


#loai bo cac khoang trang du thua trong tieu de
f = open('youtubelist0000.txt', 'r')
f2 = io.open('list_nor.txt', 'w', encoding = 'utf-8')
for line in f:
    title = line.split(';')[0]
    title_nor = " ".join(title.split())
    newline = unicode(title_nor, encoding = 'utf-8') + ";;;" + line.split(';')[3]
    f2.write(newline)