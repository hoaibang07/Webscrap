import io

def main():
    list_link = []
    for line in f:
        link = line.split(';')[3]

        #neu da co bai hat giong voi ten thi khong them vao nua
        if link not in list_link:
            list_link.append(link)
            f2.write(u'' + unicode(line, encoding = 'utf-8'))
        else:
            f3.write(u'' + unicode(line, encoding = 'utf-8'))
if __name__ == '__main__':
    f = open('youtubelist0000.txt','r')
    f2 = io.open('youtubelist0000_new.txt','w', encoding = 'utf-8')
    f3 = io.open('youtubelist0000_trunglink.txt','w', encoding = 'utf-8')
    main()
    f.close()
    f2.close()
    f3.close()