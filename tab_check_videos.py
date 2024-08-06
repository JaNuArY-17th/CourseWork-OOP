import tkinter as tk
from tkinter import *
from video_library import lib
from PIL import Image, ImageTk


class CheckVideos(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        list_videos_btn = tk.Button(self, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(self, text="Video Info").grid(row=0, column=3)

        self.videos_list_txt = Listbox(self, width=48, height=15, selectmode=SINGLE, exportselection=0)
        self.videos_list_txt.grid(row=1, column=0, columnspan=3, sticky=W, padx=10)
        self.videos_list_txt.bind("<<ListboxSelect>>", self.__on_select)

        self.video_txt = Text(self, width=30, height=4)
        self.video_txt.grid(row=1, column=3, sticky=NW, padx=10)

        self.video_image_label = Label(self)
        self.video_image_label.grid(row=1, column=3, rowspan=2, padx=10, sticky=SW)

        self.list_videos_clicked()

    
    def set_text(self, text_area, content):
        text_area.delete("1.0", tk.END)
        text_area.insert(1.0, content)

    def __on_select(self, event):
        selected_index = self.videos_list_txt.curselection()[0]
        video_str = self.videos_list_txt.get(selected_index)
        key = video_str.split(" ")[0]
        
        self.video_txt.config(state=NORMAL)
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"Name: {name}\nDirector: {director}\nRating: {rating}\nPlays: {play_count}"
            self.set_text(self.video_txt, video_details)
        else:
            self.set_text(self.video_txt, f"Video not found")
        self.video_txt.config(state=DISABLED)

        self.update_video_image(key)

    def update_video_image(self, key):
        image_path = lib.get_image_path(key)

        try:
            image = Image.open(image_path)
            image.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(image)

            self.video_image_label.config(image=photo)
            self.video_image_label.image = photo  # Keep a reference to avoid garbage collection
        except Exception as e:
            self.video_image_label.config(image='', text='Image not available')

    def list_videos_clicked(self):
        video_list = lib.list_all()
        lines = video_list.split('\n')
        self.videos_list_txt.delete(0, tk.END)
        for line in lines:
            self.videos_list_txt.insert(tk.END, f"{line}\n")

