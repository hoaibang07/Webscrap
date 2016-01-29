import io
import os.path


def check_numline(filename):
    urlsach_list = []
    urlsach_file = open(filename, 'r')
    for line in urlsach_file:
        urlsach_list.append(line.strip())
    _len = len(urlsach_list)
    return _len


def main():
    f = io.open('check_thieuchuong_output.txt', 'w', encoding = 'utf-8')
    
    for x in xrange(1,67):
        #kiem tra xem file nam co ton tai trong thu muc partcomplete hay khong
        fname = 'urlsach/data/partcomplete/sach' + str(x) + '.txt'
        if os.path.isfile(fname):
            print('ton tai sach %d'%x)
            urlsach = 'urlsach/sach' + str(x) + '.txt'

            #kiem tra so dong cua url sach, tuong ung voi so chuong
            numline = check_numline(urlsach)
            print numline

            #doc data tu file sach data
            data = open(fname).read()

            #kiem tra xem moi dong trong file sach data da co chuong cac so nay chua
            for i in xrange(1,numline + 1):
                key = str(i)
                # print ('da chay den day')
                if key not in data:
                    out = u'Sach ' + str(x) + ' thieu chuong ' + key
                    print(out)
                    f.write(out + '\n')
            
    f.close()

if __name__ == '__main__':
    main()