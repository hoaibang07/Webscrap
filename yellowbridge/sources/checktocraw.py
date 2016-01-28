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
    f = io.open('check_to_crawler_output.txt', 'w', encoding = 'utf-8')
    
    for x in xrange(1,67):
        #kiem tra xem file da duoc craw chua
        fname = 'urlsach/data/complete/sach' + str(x) + '.txt'
        f2name = 'urlsach/data/partcomplete/sach' + str(x) + '.txt'
        if os.path.isfile(fname) or os.path.isfile(f2name):
            pass
        else:
            out = u'sach ' + str(x) + ' se phai craw'
            print out
            f.write(out+'\n')
    f.close()

if __name__ == '__main__':
    main()