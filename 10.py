# write a function which will be able to read a image file and show it to you .

def imagereader(filepath):
	"""It will show image to you by entering specific path"""
	from PIL import Image
	x = Image.open(filepath)
	return x.show()
	
if __name__ == "__main__":
	imagereader(input("Enter the PATH of the image\n"))
