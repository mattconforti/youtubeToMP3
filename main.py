"""
main.py - the main file for youtubeMP3downloader
By: Matt Conforti
10/31/19
"""


# imports -------
import youtubeToMP3
from driveAPIConnect import *
from driveAPIWrite import *

# main code -------
youtubeToMP3.convertURLs()
userCredentials = authorizeUser(READONLYSCOPES)
apiResponse = apiCall(userCredentials)

fileIDList = analyzeResults(apiResponse)
parentFolderID = fileIDList[0]

if youtubeToMP3.debug:
    print('\nParent Folder ID: %s' % parentFolderID)

newFilesList = getUploadData()  # get list of files to upload
if youtubeToMP3.debug:
    for file in newFilesList:
        print(file)

uploadBool = input('\n-------\nUPLOAD? (Y/N): ')
print('-------\n')

if uploadBool == 'Y':
    for file in newFilesList:
        newUpload = uploadFile(file)
        if youtubeToMP3.debug:
            print(newUpload)
        newUpdate = updateFile(file, newUpload['id'], parentFolderID)  # update the file's parents
        if youtubeToMP3.debug:
            print('\nUpdated file: %s' % newUpdate)
else:
    print("Download Successful.")
    exit(0)
