import os

class Dir_Handler:
	def __init__(self):
		"""
		Utility class for managing the directories of the exported captures
		"""

		self.parent_dir = "/home/capstone/Documents/Captures"
		self.export_dirname = "Capture"

		os.makedirs(self.parent_dir, exist_ok=True)

	def locate_export_dir(self, filename):
		"""
		For a file with a given name, find and return an export folder for it to be saved to
		Will either find an existing available folder or create a new one

		@filename: Name of the file, excluding timestamps
		"""
		all_dirs = list(filter(lambda d: self.export_dirname in d, next(os.walk(self.parent_dir))[1]))
		
		# If no directories exist
		if len(all_dirs) == 0:
			return self.create_new_export_dir(0)

		# Now at least one directory exists, find latest one
		latest_dirname = max(all_dirs)
		latest_dir = f"{self.parent_dir}/{latest_dirname}"

		# If latest directory is not already used
		latest_dir_files = next(os.walk(latest_dir))[2]
		if len(list(filter(lambda f: filename in f, latest_dir_files))) == 0:
			return latest_dir

		# Now must create a new dir
		latest_dirnum = int(latest_dirname.split("_")[-1])
		return self.create_new_export_dir(latest_dirnum+1)
		

	def create_new_export_dir(self, num):
		"""
		Create a new empty folder

		@num: Integer to suffix the folder name
		"""
		new_dirname = f"{self.parent_dir}/{self.export_dirname}_{str(num).zfill(3)}"
		os.makedirs(new_dirname, exist_ok=True)
		return new_dirname
