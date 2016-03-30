import sys

def main():
    filename = sys.argv[-1]
    f = open(filename, 'r');
    seen = set()
    count = 0
    for line in f:
        count += 1
        line_lower = line.lower()
        if line_lower in seen:
            print("Dong lap: %d"%count);
            # break;
        else:
            seen.add(line_lower);
    
if __name__ == '__main__':
    main()