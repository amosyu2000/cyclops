import os

class Dir_Handler:
	def __init__(self):
		"""
		Utility class for managing the directories of the exported captures
		"""

		self.rpi_dir = "/home/capstone/Documents"
		self.usb_dir = "/media/usb"
		self.parent_dirname = "Captures"
		self.export_dirname = "Capture"

	def get_parent_dir(self):
		"""
		Returns the path of the parent capture directory
		Will either be a path to the mounted USB drive directory or to the Raspberry Pi directory  
		"""
		parent_dir = f"{self.usb_dir if self.mount_usb_drive() else self.rpi_dir}/{self.parent_dirname}"
		os.makedirs(parent_dir, exist_ok=True)
		return parent_dir

	def mount_usb_drive(self):
		"""
		Tries to mount a USB drive, and returns True if successful
		"""
		device_name = self.find_usb_drive()
		# If no USB drive is detected
		if device_name == None:
			return False
		# Check all the mounts of the Raspberry Pi
		mounts_file = open("/proc/mounts")
		lines = mounts_file.readlines()
		mounts_file.close()
		# If the connected USB drive is not the one that is mounted
		if not next((True for line in lines if line.find(f"{device_name} {self.usb_dir}") != -1), False):
			# Unmount all old USB drives
			[os.system(f"umount {self.usb_dir}") for line in lines if line.find(self.usb_dir) != -1]
			# Mount the connected USB drive
			os.system(f"mount {device_name} {self.usb_dir}")
		return True

	def find_usb_drive(self):
		"""
		Find a USB flash drive. Returns the device name, or None if no device was found
		https://raspberrypi.stackexchange.com/a/132399
		"""

		partitions_file = open("/proc/partitions")
		# Skips header lines
		lines = partitions_file.readlines()[2:]
		partitions_file.close()
		for line in lines:
			words = [word.strip() for word in line.split()]
			minor_number = int(words[1])
			device_name = words[3]
			# The minor_number of a USB drive is always a multiple of 16 (ex. 0, 16, ...)
			if minor_number % 16 == 0:
				path = f"/sys/class/block/{device_name}"
				# Differentiates between USB drive and other devices (i.e. ram)
				if os.path.islink(path) and os.path.realpath(path).find("/usb") != -1:
					return f"/dev/{device_name}1"
		return None

	def locate_export_dir(self):
		"""
		For a file with a given name, create and return an export folder for it to be saved to
		"""
		all_dirs = list(filter(lambda d: self.export_dirname in d, next(os.walk(self.get_parent_dir()))[1]))
		
		# If no directories exist
		if len(all_dirs) == 0:
			return self.create_new_export_dir(0)

		# Now at least one directory exists, find latest one
		latest_dirname = max(all_dirs)

		# Now must create a new dir
		latest_dirnum = int(latest_dirname.split("_")[-1])
		return self.create_new_export_dir(latest_dirnum+1)

	def create_new_export_dir(self, num):
		"""
		Create a new empty folder

		@num: Integer to suffix the folder name
		"""
		new_dirname = f"{self.get_parent_dir()}/{self.export_dirname}_{str(num).zfill(3)}"
		os.makedirs(new_dirname, exist_ok=True)
		return new_dirname
