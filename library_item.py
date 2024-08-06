class LibraryItem:
    def __init__(self, name, director, rating, time, image_path=None):
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = time
        self.image_path = image_path

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == '':
            raise ValueError('Name can not be empty')
        self.__name = name

    @property
    def director(self):
        return self.__director
    
    @director.setter
    def director(self, director):
        if director == '':
            raise ValueError('Director can not be empty')
        self.__director = director

    @property
    def rating(self):
        return self.__rating
    
    @rating.setter
    def rating(self, rate):
        if rate > 5 or rate < 0:
            raise ValueError('Rating must be a number smaller or equal to 5 and greater or equal than 0')
        self.__rating = rate

    @property
    def play_count(self):
        return self.__play_count
    
    @property
    def image_path(self):
        return self.__image_path
    
    @image_path.setter
    def image_path(self, image_path):
        if image_path == '':
            raise ValueError('Image path can not be empty')
        self.__image_path = image_path
    
    @play_count.setter
    def play_count(self, time):
        if time < 0:
            raise ValueError('Number of play must be a number greater or equal to 0')
        self.__play_count = time

    def info(self):
        return f"{self.name} - {self.director} - {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars

    def __str__(self) -> str:
        return f"{self.name},{self.director},{self.rating},{self.play_count},{self.image_path}".strip()


