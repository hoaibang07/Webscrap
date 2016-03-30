import os
from os import listdir
from os.path import isfile, join
import io

def main():
    #get current directory
    current_dir = os.path.dirname(os.path.realpath(__file__))
    #bien list_filename luu tat ca ten file trong thu muc hien thoi
    list_filename = []
    for file_ in listdir(current_dir):
        if isfile(file_):
            if(file_ != "removedonglap.py"):
                print file_
if __name__ == '__main__':
    main()