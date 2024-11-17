import requests
from datetime import datetime

class Project:
    def __init__(self, id: str):
        '''
        __init__ creates a new project object.

        :param id: The ID or slug of the project.
        '''

        r = requests.get(f'https://api.modrinth.com/v2/project/{id}')
        if r.status_code == 404:
            raise FileNotFoundError

        # Parse out data
        data = r.json()

        self.id = data['id']
        self.team = data['team']
        self.moderatorMsg = data['moderator_message']

        self.publishedAt = datetime.fromisoformat(data['published'])
        self.updatedAt = datetime.fromisoformat(data['updated'])
        self.approvedAt = datetime.fromisoformat(data['approved'])
        if data['queued'] != None:
            self.queuedAt = datetime.fromisoformat(data['queued'])

        self.followers = data['followers']
        self.license = data['license']
        self.versionIDs = data['versions']
        self.gameVersions = data['game_versions']
        self.modLoaders = data['loaders']
        self.galleryImages = data['gallery']
