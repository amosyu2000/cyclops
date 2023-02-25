# to embrace the grand powers of folder deletion
# you must become su ... sudo su
# eheheheeeheheeeh
import os
import shutil

def delete(path):
    folders = os.listdir(path)
    for folder in folders:
        shutil.rmtree(path + folder)

# file
delete('/home/capstone/Documents/Captures/')