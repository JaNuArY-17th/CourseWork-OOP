from library_item import LibraryItem

class LibraryItemEpisode(LibraryItem):
    def __init__(self, name, director, rating, time, episode):
        super().__init__(name, director, rating, time)
        self.__episode = episode

    @property
    def episode(self):
        return self.__episode
    
    @episode.setter
    def episode(self, ep):
        if ep <= 0:
            raise ValueError("Episode must be a positive number")
        self.__episode = ep

    