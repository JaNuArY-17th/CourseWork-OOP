from library_item_episode import LibraryItemEpisode
from video_library import VideoLibrary

class EpisodeLibrary(VideoLibrary):
    def __init__(self, name):
        super().__init__(name)
    
    def import_library(self):
        with open('episode.txt', 'r') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                currentline = lines[i].split(",")
                episode = LibraryItemEpisode(str(currentline[0]), str(currentline[1]), int(currentline[2]), int(currentline[3]), int(currentline[4]))
                self._library[str(i + 1)] = episode

    def check_episode(self, ep):
        for ep in self._library:
            if ep.episode == ep:
                return 1
        return 0

ep_lib = EpisodeLibrary('Episodes Library')
ep_lib.import_library()
