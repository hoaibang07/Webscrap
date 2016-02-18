import io
import re

def main():
    list_songName = []
    list_youtube = []
    for line in song_name_file:
        list_songName.append(line)
    for line in youtube_list_file:
        list_youtube.append(line)
    len_ = len(list_songName)
    j = 0
    for x in xrange(0,len_):
        song = list_songName[x]
        line1 = song.strip() + ';;;' + list_youtube[j].strip()
        #nomalize string
        pat = re.compile(r'\s+')
        line1 = pat.sub(' ', line1)
        out_file.write(unicode(line1 + '\n', encoding = 'utf-8'))
        j = j + 1
        line2 = song.strip() + ';;;' + list_youtube[j].strip()
        #nomalize string
        # pat = re.compile(r'\s+')
        line2 = pat.sub(' ', line2)
        out_file.write(unicode(line2 + '\n', encoding = 'utf-8'))
        j = j + 1

if __name__ == '__main__':
    youtube_list_file = open('youtubelist_0.txt', 'r')
    song_name_file = open('songName0.txt', 'r')
    out_file = io.open('skplayer_list.txt', 'w', encoding = 'utf-8')
    main()
    youtube_list_file.close()
    song_name_file.close()
    out_file.close()