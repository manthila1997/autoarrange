import os
import glob

files_list = glob.glob("*")

extension_set = set()

#adding each type of extension to the set
for file in files_list:
    name = file[::-1]
    extension = name.split(sep=".")
    try:
        extension_set.add(extension[1])
    except IndexError:
        continue

#print(extension_set)
#Function to create directory for each type of extension
def createDirs():
    for dir in extension_set:
        try:
            os.makedirs(dir+"_files")
        except FileExistsError:
            continue

#Function to move files to respective folders
def arrange():
    for file in files_list:
        fextension = file.split(sep=".")
        try:
            os.rename(file, fextension[1]+"_files/"+file)
        except (OSError, IndexError):
            continue

#Calling the functions in order
createDirs()
arrange()
