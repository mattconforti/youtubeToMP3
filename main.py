"""
main.py - the main file for youtubeMP3downloader
By: Matt Conforti
10/31/19
"""


# imports -------
import youtubeToMP3
from driveAPIWrite import *

# main code -------
youtubeToMP3.convertURLs()
parentFolder = "1bCYIwkcGb0D0Ha3nGVUhZ8rO6caB8InJ"
newFilesList = getUploadData()
for file in newFilesList:
    print(file)

uploadBool = input('\n-------\nUPLOAD? (Y/N): ')
print('-------\n')

if uploadBool == 'Y':
    for file in newFilesList:
        newUpload = uploadFile(file)
        print(newUpload)
        newUpdate = updateFile(file, newUpload['id'], parentFolder)  # update the file
        print('\nUpdated file: %s' % newUpdate)
else:
    print("Download Successful.")
    exit(0)
