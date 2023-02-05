import time

def print_handler(domain, string):
	"""
	Utility function for more cleaner, time-stamped prints to the terminal

	@domain: The category of the print message
	@string: The actual message to print
	"""
	
	print(f"{time.ctime()}: [{domain}] {string}")