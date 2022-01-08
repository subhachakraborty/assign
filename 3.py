# Write a function which will take input as a dict and give me out as a list of all the values
# even in case of 2 level nesting it should work .
def func(a):
	"""It will take input as a dict and give me out as a list of all the values"""
	if type(a) == dict:
		l = []
		for i in a:
			if type(a[i]) == dict:
				for j in a[i]:
					l.append(a[i][j])
			else:
				l.append(a[i])
		return l
	else:
		return "Please enter a dictionary not ",type(a)

if __name__ == "__main__":
	print(func({"a":243,"b":"312","c":["312","dsa"],"d":{"fds":"asaf","asas":8}}))
	print(func("X"))
