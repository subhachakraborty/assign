# write a function which can help you to filter only word file from a directory .

import os

def wordfile(path):
    l = []
    listoffile = os.listdir(path)
    for i in listoffile:
        if i[-1:-5:-1] == "xcod" or i[-1:-4:-1] == "cod":
            l.append(i)
    return l

if __name__ == "__main__":
    print(wordfile("C:\\Users\\subha\\Downloads\\"))