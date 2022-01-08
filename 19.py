# write a function by which you can print an ip address of your system .
# https://docs.python.org/3.9/howto/ipaddress.html#ipaddress-howto
from os import system
import platform

def ipaddressdetail():
    """Print details of your ip address"""
    if platform.system() == "Windows":
        system("ipconfig")
    else:
        system("ifconfig")

if __name__ == "__main__":
    ipaddressdetail()