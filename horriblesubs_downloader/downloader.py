from urllib.request import urlretrieve
import os

class Downloader(object):
    def __init__(self, anime_info):
        self.name = anime_info['name']
        self.episodes = anime_info['episodes']
        self.resolution = anime_info['resolution']
        self.links = anime_info['links']

    def download(self, folder):
        if self.episodes == 'batch':
            self.episodes = range(1, len(self.links) + 1)
        pairs = zip(self.episodes, self.links)
        for pair in pairs:
            episode = int(pair[0])
            if episode < 10:
                episode = '0' + str(episode)
            file_name = '[HorribleSubs] {} - {} [{}p].torrent'.format(self.name, episode, self.resolution)
            urlretrieve(pair[1], os.path.join(folder, file_name))
