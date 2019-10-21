"""
youtubeToMP3.py - allows user to convert youtube videos
into mp3 files for download
By: Matt Conforti
10/21/19
"""


# imports -------
import youtube_dl


# functions -------

def getURLInput():
    """
    Creates a list of strings input by the user and returns it
    :return urlList: the list of input strings
    """
    exitPhrases = ['download', 'stop', 'quit', 'exit']
    urlList = []
    usrIn = input('\nURL: ')
    while usrIn not in exitPhrases:
        urlList.append(usrIn.strip())
        usrIn = input('URL: ')
    return urlList


def download(ydlOptions, urlList):
    """
    Uses youtube_dl's download function to process the given list
    :param ydlOptions: a dict containing settings for the download
    :param urlList: the list of URL's to download
    """
    with youtube_dl.YoutubeDL(ydlOptions) as ydl:
        ydl.download(urlList)


def main():
    print('\nEnter YouTube URLs below.')
    urlList = getURLInput()
    ydlOpts = {'format': 'bestaudio/best',
               'nocheckcertificate': True,
               'noplaylist': True,
               'postprocessors': [{'key': 'FFmpegExtractAudio',
                                   'preferredcodec': 'mp3',
                                   'preferredquality': '192', }],
               }
    download(ydlOpts, urlList)


# main code -------
if __name__ == '__main__':
    main()
