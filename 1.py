# 1 . you have to write a fun which will take string and return a len of
# it without using a inbuilt fun len
def length(string):
    """Returns number of character in a string"""
    if type(string) == str:
        count = 0
        for i in string:
            count += 1
        return count
    else:
        return "It is not a string" 


if __name__ == "__main__":
    print(length("a"))
