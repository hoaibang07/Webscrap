import io

def main():
    list_songName = []
    for line in f:
        songName = line.split('|')[1]

        #neu da co bai hat giong voi ten thi khong them vao nua
        if songName not in list_songName:
            list_songName.append(songName)
            f2.write(u'' + unicode(songName, encoding = 'utf-8') + '\n')
        else:
            f3.write(u'' + unicode(songName, encoding = 'utf-8') + '\n')
if __name__ == '__main__':
    f = open('kara_list1_1.txt','r')
    f2 = io.open('kara_list1_1_songName_Moi.txt','w', encoding = 'utf-8')
    f3 = io.open('kara_list1_1_songName_trungTen_Moi.txt','w', encoding = 'utf-8')
    main()
    f.close()
    f2.close()
    f3.close()