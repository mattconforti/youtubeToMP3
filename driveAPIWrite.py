"""
driveAPIWrite.py - connects to Google Drive API and uploads files
for use in youtubeToMP3.py
By: Matt Conforti
10/23/19
"""


# imports -------
import os
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
    pass


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
    fileMedia = MediaFileUpload(fileName, mimetype='audio/mpeg', resumable=True)

    fileUploaded = service.files().create(body=fileMetaData,
                                          media_body=fileMedia,
                                          fields='id').execute()
    return fileUploaded


def main():
    # fileNames = getUploadData()
    #  for file in fileNames:
    #      uploadFile(file)

    # test
    parentFolder = driveAPIConnect.PARENTID
    newUpload = uploadFile("/Users/mattconforti/newMusic/LilTjay-Ruthless.mp3", parentFolder)
    print(newUpload)


# main code -------
if __name__ == '__main__':
    main()
