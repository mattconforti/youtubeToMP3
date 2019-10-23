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


# functions -------
def getUploadData():
    """
    Retrieves a list of fileNames to be uploaded from the OS
    :return: fileList: the list of fileNames to upload
    """
    pass


def uploadFile(fileName):
    """
    Performs a 'simple upload' by connecting to the Drive API
    :param fileName: the name of the file for upload (with extension)
    :return: fileUploaded: the file resource object returned by the API .create call
    # TODO: use parents parameter in service.files().create() to upload file to correct place
    """
    usrCreds = driveAPIConnect.AuthorizeUser()  # get credentials
    service = build('drive', 'v3', credentials=usrCreds)  # build API service

    fileMetaData = {'name': fileName}
    fileMedia = MediaFileUpload(fileName, mimetype='audio/mpeg')

    fileUploaded = service.files().create(body=fileMetaData,
                                          media_body=fileMedia,
                                          fields='id').execute()
    return fileUploaded


def main():
    # fileNames = getUploadData()
    #  for file in fileNames:
    #      uploadFile(file)
    pass


# main code -------
if __name__ == '__main__':
    main()
