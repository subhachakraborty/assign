# write a fun which will be able to print an index of all primitive element which you will pass
def indexofall(a):
    if type(a) == str or type(a) == list or type(a) == tuple :
        count = 0
        for i in a:
            print((count,i))
            count += 1
    else:
        print(type(a),"is not indexable")   

if __name__ == "__main__":  
    indexofall([1,2,True,"hf"])