import urllib.request
import generateUniqueId


def getImagePath(url):
    filename = generateUniqueId.getUniqueId()
    filepath = str(filename) + '.png'
    urllib.request.urlretrieve(url, filepath)
    return filepath
