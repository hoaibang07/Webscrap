import io

urlsach_file = open('urlsach.txt', 'r')
num_lines = sum(1 for line in urlsach_file)
print('Total lines in urlsach.txt: %d'%num_lines)