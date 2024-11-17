import requests

def getLabrinthVersion() -> str:
    '''
    getLabrinthVersion gets the current online version of the Labrinth API.

    :return: version number as a string.
    '''

    r = requests.get('https://api.modrinth.com')
    return r.json()['version']