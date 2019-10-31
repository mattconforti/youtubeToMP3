"""
driveAPIWrite.py - connects to Google Drive API and uploads files
for use in youtubeToMP3.py
By: Matt Conforti
10/23/19
"""


# imports -------
import os
import datetime as dt
import driveAPIConnect
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# SCOPES - if modified delete token.pickle
READWRITESCOPES = ['https://www.googleapis.com/auth/drive']


# functions -------
def getUploadData():
    """
    Retrieves a list of fileNames to be uploaded from the OS
    :return: fileList: the list of fileNames to upload
    """
    fileList = []
    currentDateTime = dt.datetime.now()
    timeAgo = currentDateTime - dt.timedelta(minutes=5)  # 5 minute window of seeing new files
    print('\nGetting files as of %s...' % timeAgo)
    dirList = (os.listdir('/Users/mattconforti/Desktop/CSC/Python/youtubeMP3downloader'))
    print('\nFile List:')
    for item in dirList:
        if item.__contains__('.mp3'):
            st = os.stat(item)
            ctime = dt.datetime.fromtimestamp(st.st_ctime)
            if ctime > timeAgo:  # list songs that are created < 1 min ago
                fileList.append(item)

    for file in fileList:
        print(file)


def uploadFile(fileName, parentID):
    """
    Performs a 'simple upload' by connecting to the Drive API
    :param fileName: the name of the file for upload (with extension)
    :param parentID: the id of the upload destination folder
    :return: fileUploaded: the file resource object returned by the API .create call
    """
    usrCreds = driveAPIConnect.authorizeUser(READWRITESCOPES)  # get credentials
    service = build('drive', 'v3', credentials=usrCreds)  # build API service

    fileMetaData = {'name': fileName, 'parents': [{'id': parentID}]}
    fileMedia = MediaFileUpload(fileName, mimetype='audio/mpeg')

    fileUploaded = service.files().create(body=fileMetaData,
                                          media_body=fileMedia,
                                          fields='id').execute()
    return fileUploaded
