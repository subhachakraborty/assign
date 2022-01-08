# write a function which will be able to take a list as an input return an index of each element
# like a inbuilt index function but even if we have repetative element it should return index

def indexoflist(a):
	"""It will be able to take a list as an input return an index of each element
   like a inbuilt index function but even if we have repetative element it should return index"""
	l = []
	count = 0
	for i in a:
		l.append((i,count))
		count = count + 1
	return l

if __name__ == "__main__":
	print(indexoflist(["a","b","a"]))
