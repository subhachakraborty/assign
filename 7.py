 # Write a function which will whould return list of all the file name from a directory .
import os
ls = []
def listoffile(directory):
    """It will return list of all the file name from a directory"""
    filelist = os.listdir(directory)
    return directory,filelist

def filterfolder(x):
    directory = x[0]
    filelist = x[1]
    for i in filelist:
        try:
            os.listdir(directory+"//"+i)
            filterfolder(directory+"//"+i,os.listdir(directory+"//"+i))
        except:
            ls.append(i)
    return ls


if __name__ == "__main__":
    print(filterfolder(listoffile("./")))
    
# ./ ---> current directory, . ---> drive where python is installed