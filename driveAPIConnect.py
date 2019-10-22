"""
driveAPIConnect.py - connects to Google Drive API
for use in youtubeToMP3.py (with code from https://developers.google.com/drive/api/v3/quickstart/python
and https://developers.google.com/drive/api/v3/about-auth)
By: Matt Conforti
10/21/19
"""


# imports -------
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# SCOPES - if modified delete token.pickle
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']


def main():
    """
    Prints the names and ids of the first 10 files the user has access to.
    TODO: split into authorize, connect, and print functions
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API and get a list of folders
    # use service.files.list with appropriate parameters - returns a dict
    results = service.files().list(q="name='NEW MUSIC'",
                                   spaces="drive").execute()

    # obtain list of files from results
    items = results.get('files', [])

    if not items:
        print("No files were found.")
    else:
        for item in items:
            print('\n%s' % item['name'])


if __name__ == '__main__':
    main()
