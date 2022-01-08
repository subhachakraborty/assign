# write a function which will be able to shutdown your system .

import os
def windows_shutdown():
    """It will shutdown your system if your system is windows"""
    #https://www.ionos.com/digitalguide/server/configuration/shutdown-commands-via-cmd/
    x = input("Do You really want to shutdown the system? Type Yes or No\n")
    if x.lower() == "yes":
        os.system("shutdown /s /t 60")
        print("The system will shutdown in 1 min")
    elif x.lower() == "no":
        exit()
    else:
        print("please enter correct command")
        exit()
def linux_shutdown():
    """It will shutdown your system if your system is other than windows"""
    x = input("Do You really want to shutdown the system? Type Yes or No\n")
    if x.lower() == "yes":
        os.system("sudo shutdown")
        print("The system will shutdown in 1 min")
    elif x.lower() == "no":
        exit()
    else:
        print("please enter correct command")
        exit()

def shutdown():
    """It will shutdown your system after 1 min"""
    import platform
    if platform.system() == "Windows":
        windows_shutdown()
    else:
        linux_shutdown()

if __name__ == "__main__":
    shutdown()
