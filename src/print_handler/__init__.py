import time
from colorama import Fore, Back, Style

def print_handler(domain, string):
	"""
	Utility function for more cleaner, time-stamped prints to the terminal

	@domain: The category of the print message
	@string: The actual message to print
	"""
	# color coding based on domain
	if domain == "Main":
		print(Fore.WHITE + f"{time.ctime()}: " + Fore.RED + f"[{domain}] {string}")
	elif domain == "Thread - Acceleration":
		print(Fore.WHITE + f"{time.ctime()}: " + Fore.GREEN + f"[{domain}] {string}")
	elif domain == "Thread - Camera":
		print(Fore.WHITE + f"{time.ctime()}: " + Fore.CYAN + f"[{domain}] {string}")
	elif domain == "Thread - Lidar":
		print(Fore.WHITE + f"{time.ctime()}: " + Fore.PURPLE + f"[{domain}] {string}")
	elif domain == "Thread - Capture":
		print(Fore.WHITE + f"{time.ctime()}: " + Fore.BLUE + f"[{domain}] {string}")
	else:
		print(Fore.WHITE + f"{time.ctime()}: [{domain}] {string}")