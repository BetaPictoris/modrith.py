#!/usr/bin/env python3
# -*- coding: utf8 -*-

import requests
from warnings import warn

__version__ = '1.0.0'

LABRINTH_BASE_URL = 'https://api.modrinth.com'

def getLabrinthVersion() -> str:
    '''
    getLabrinthVersion gets the current online version of the Labrinth API.
    '''

    r = requests.get(LABRINTH_BASE_URL + '/')
    return r.json()['version']