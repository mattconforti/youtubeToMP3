"""
youtubeToMP3.py - allows user to convert youtube videos
into mp3 files for download
By: Matt Conforti
10/21/19
"""


# imports -------
import youtube_dl


# global vars -------
debug = True


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


def download(ydlOptions, url):
    """
    Uses youtube_dl's download function to process the given URL
    :param ydlOptions: a dict containing settings for the download
    :param url: the URL of the song
    :return urlInfo: a dict containing information about the song
    """
    with youtube_dl.YoutubeDL(ydlOptions) as ydl:
        urlInfo = ydl.extract_info(url, download=True)
        return urlInfo


def main():
    print('\nEnter YouTube URLs below.')
    urlList = getURLInput()
    ydlOpts = {'format': 'bestaudio/best',
               'no_warnings': True,
               'nocheckcertificate': True,
               'noplaylist': True,
               'postprocessors': [{'key': 'FFmpegExtractAudio',
                                   'preferredcodec': 'mp3',
                                   'preferredquality': '192', }],
               }

    for item in urlList:
        itemInfo = download(ydlOpts, item)
        artist = itemInfo.get('creator')
        title = itemInfo.get('alt_title')
        print('\nArtist: %s\nTitle: %s\n' % (artist, title))
        if debug:
            print(itemInfo)


# main code -------
if __name__ == '__main__':
    main()
