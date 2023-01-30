import time

def print_handler(domain, string):
	"""
	Utility function for cleaner prints to the terminal
	"""
	
	print(f"{time.ctime()}: [{domain}] {string}")