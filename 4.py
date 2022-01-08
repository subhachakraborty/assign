# write a fun which will take another function as an input and return me an output

def add(x,y):
	"""Add two number and returns the output"""
	if type(x)== int or type(x) == float:
		if type(y)== int or type(y) == float:
			return x+y
		
		else:
			return "Please use proper parameter"
	else:
		return "Please use proper parameter"

def squareofsum(x,y):
	"""return square of sum of two numbers"""
	if add(x, y) != "Please use proper parameter":
		return add(x, y)**2
	else:
		return "Error"

if __name__ == "__main__":
	print(squareofsum(3,8))