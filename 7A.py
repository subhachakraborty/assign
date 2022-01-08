 # Write a function which will whould return list of all the file name from a directory .
def listoffile(directory):
    """It will return list of all the file name from a directory"""
    import os
    ls = []
    filelist = os.listdir(directory)
    for i in filelist:
        try:
            os.listdir(directory+"//"+i)
        except:
            ls.append(i)
    return ls


if __name__ == "__main__":
    print(listoffile(input("Enter the PATH of the directory\n")))
    
# ./ ---> current directory, . ---> drive where python is installed