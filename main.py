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
#newUpload = uploadFile("Dave East - Godfather 4.mp3", parentFolder)
#print(newUpload)
