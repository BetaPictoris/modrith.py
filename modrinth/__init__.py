#!/usr/bin/env python3
# -*- coding: utf8 -*-
__version__ = '1.0.0'


import requests

from .project import *

def getLabrinthVersion() -> str:
    '''
    getLabrinthVersion gets the current online version of the Labrinth API.

    :return: version number as a string.
    '''

    r = requests.get('https://api.modrinth.com')
    return r.json()['version']