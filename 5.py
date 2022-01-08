# write a function which will take multiple list as a input 
# and give me concatnation of all the element and output

def addlist(*lists):
    """It will take multiple list as a input and give concatnation of all the element and output"""
    l = []
    for i in lists:
        l.extend(i)

    return l

if __name__ == "__main__":
    print(addlist([1,3,6],[5,9],["k"]))