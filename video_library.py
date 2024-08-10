from library_item import LibraryItem

class VideoLibrary:
    def __init__(self, name):
        self.name = name
        self.__library = {}

        f = open('library.txt', 'r')
        lines = f.readlines()
        for i in range(len(lines)):
            currentline = lines[i].split(",")
            video = LibraryItem(str(currentline[0]), str(currentline[1]), int(currentline[2]), int(currentline[3]), str(currentline[4]) if len(currentline) > 4 else None)
            self.__library[str(i + 1)] = video

    @property
    def library(self):
        return self.__library

    def list_all(self):
        output = ""
        for key in self.__library:
            item = self.__library[key]
            output += f"{key} {item.info()}\n"
        return output


    def get_info(self, key):
        try:
            item = self.__library[key]
            return item
        except KeyError:
            return None


    def get_name(self, key):
        try:
            item = self.__library[key]
            return item.name
        except KeyError:
            return None


    def get_director(self, key):
        try:
            item = self.__library[key]
            return item.director
        except KeyError:
            return None


    def get_rating(self, key):
        try:
            item = self.__library[key]
            return item.rating
        except KeyError:
            return -1


    def set_rating(self, key, rating):
        try:
            item = self.__library[key]
            item.rating = rating

            with open('library.txt', 'r') as f:
                lines = f.readlines()
                currentline = lines[int(key) - 1].split(',')
                lines[int(key) - 1] = lines[int(key) - 1].replace(currentline[2], f"{str(rating)}")

            with open('library.txt', 'w') as f:
                f.writelines(lines)
        except KeyError:
            return


    def get_play_count(self, key):
        try:
            item = self.__library[key]
            return item.play_count
        except KeyError:
            return -1


    def increment_play_count(self, key):
        try:
            item = self.__library[key]
            item.play_count += 1

            with open('library.txt', 'r') as f:
                lines = f.readlines()
                currentline = lines[int(key) - 1].split(',')
                lines[int(key) - 1] = lines[int(key) - 1].replace(currentline[3], f"{str(item.play_count)}\n")

            with open('library.txt', 'w') as f:
                f.writelines(lines)
        except KeyError:
            return

    def check_video(self, video):
        for vid in self.__library:
            if video.name.lower() == self.__library[vid].name.lower() and video.director.lower() == self.__library[vid].director.lower():
                return 1
        return 0

    def add_video_to_library(self, name, director, rating, image_path):
        video = LibraryItem(name, director, rating, 0, image_path)
        if self.check_video(video) == 1:
            raise ValueError("Video existed")
        else:
            with open('library.txt', 'r') as f:
                lines = f.readlines()
                self.__library[str(len(lines)+1)] = video

            with open('library.txt', 'a') as f:
                if not lines[-1]:
                    f.write(f"{video}")
                else:
                    f.write("\n")
                    f.write(f"{video}")

    def delete_video_from_library(self, key):
        if self.get_info(key) == None:
            raise ValueError("Video not found")
        else:
            del self.__library[key]

            with open('library.txt', 'w') as f:
                first, *_, last = self.__library.values()
                for key, value in self.__library.items():
                    if value != last:
                        f.write(f"{value}\n")
                    else:
                        f.write(f"{value}")


    def get_image_path(self, key):
        try:
            item = self.__library[key]
            return item.image_path.strip()
        except KeyError:
            return None
            

lib = VideoLibrary("Library")
