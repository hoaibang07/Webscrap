import io

def main():
    list_cu = []
    list_moi = []
    for line in f:
        list_cu.append(line)
    for line in f2:
        list_moi.append(line)
    for songName in list_moi:

        #neu da co bai hat giong voi ten thi khong them vao nua
        if songName not in list_cu:
            f3.write(u'' + unicode(songName, encoding = 'utf-8'))
if __name__ == '__main__':
    f = open('kara_list1_1_songName.txt','r')
    f2 = open('kara_list1_1_songName_ToanboMoi.txt', 'r')
    f3 = io.open('danhsachmoithemvao.txt','w', encoding = 'utf-8')
    main()
    f.close()
    f2.close()
    f3.close()