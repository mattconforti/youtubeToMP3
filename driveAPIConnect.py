"""
driveAPIConnect.py - connects to Google Drive API and searches for the 'NEW MUSIC' folder
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


# functions -------
def authorizeUser():
    """
    Uses pickle module to serialize credentials
    and authenticate the user to use API services
    :return: creds: the credentials of the user
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
    return creds


def apiCall(credentials):
    """
    Make a call to the API, and query files found inside
    Google Drive until the NEW MUSIC folder is found
    :param credentials: the user's credentials
    :return: results: a dict containing a response from the API call
    """
    service = build('drive', 'v3', credentials=credentials)
    # Call the Drive v3 API and get a list of folders
    # using service.files.list with appropriate parameters ('q' is a query string)
    results = service.files().list(q="name='NEW MUSIC'", spaces="drive").execute()
    return results


def analyzeResults(apiResponse):
    """
    Print a list of files from the results as well as
    the other attributes associated with the response
    :param apiResponse: the response from apiCall()
    """
    # obtain list of files from results
    items = apiResponse.get('files', [])

    if not items:
        print('No files were found.')
    else:
        print('\nFiles:')
        for item in items:
            print('%s\n' % item['name'])

    print('Response Body:')
    print('kind: %s\nnextPageToken: %s\nincompleteSearch: %s'
          % (apiResponse.get('kind'), apiResponse.get('nextPageToken'), apiResponse.get('incompleteSearch')))


def main():
    userCredentials = authorizeUser()
    apiResponse = apiCall(userCredentials)
    analyzeResults(apiResponse)  # print the results from the API call


if __name__ == '__main__':
    main()
