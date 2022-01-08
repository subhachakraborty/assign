# write a function whihc can move a file from one directory to another directory .

def movefile(old_path,new_path):
    """It can move a file from one directory to another directory ."""
    import shutil
    shutil.move(old_path,new_path)
    return "Success"

if __name__ == "__main__":
    path1 = input("Enter the localation of file to move\n")
    path2 = input("Enter destination path\n")
    movefile(path1,path2)