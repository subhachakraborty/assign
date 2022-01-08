# write a function which will be able to show your system configuration .

def config():
	"""Show your system configuration"""
	import platform
	import psutil  #To install psutil type "pip install psutil" 
	return f"""OS is {platform.system()}\nProcessor is {platform.processor()}
Mechine is {platform.machine()}\nArchitecture is {platform.architecture()[0]}
Total ram is {psutil.virtual_memory()[0]}  byte"""

if __name__ == "__main__":
	print(config())