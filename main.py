import os
import re

DIRECTORY = '/Users/sedir/pCloud Drive/Automatic Upload/Skromeloo'


def move_file(directory, file):
    year = file[:4]
    month = file[5:7]
    if os.path.isdir(directory + '/' + year + '/' + month) is False:
        os.makedirs(directory + '/' + year + '/' + month)
    os.rename(directory + '/' + file, directory + '/' + year + '/' + month + '/' + file)


def organize_files(directory):
    regexp = re.compile('\d{4}-\d{2}-\d{2}')
    for item in os.listdir(directory):
        if os.path.isdir(directory + '/' + item) is False and regexp.match(item):
            print(item[:10], '-> filename', item)
            move_file(directory, item)


if __name__ == '__main__':
    organize_files(DIRECTORY)
