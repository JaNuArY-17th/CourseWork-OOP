import tkinter as tk
from tkinter import *
from video_library import lib
import tkinter.scrolledtext as tkst
from tkinter import messagebox as msb
import os

class CreateVideosList(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.__playlist =  []
        self.__playlist_name = []
        with open('playlist.txt', 'r') as f:
            lines = f.read().splitlines()
            for i in range(len(lines)):
                if lines[i].startswith("Playlist:"):
                    currentline = lines[i].split(": ")
                    name = str(currentline[1])
                    self.__playlist_name.append(name)
        
        create_the_playlist_btn = tk.Button(self, text="Create The Playlist", command=self.create_the_playlist_clicked)
        create_the_playlist_btn.grid(row=0, column=0, padx=10, pady=10)

        reset_the_playlist_btn = tk.Button(self, text="Reset The Playlist", command=self.reset_the_playlist_clicked)
        reset_the_playlist_btn.grid(row=0, column=3, columnspan=2, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(self, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, rowspan=4, sticky="W", padx=10, pady=10)

        enter_lbl = tk.Label(self, text="Enter Video Number")
        enter_lbl.grid(row=1, column=3, padx=10)

        self.input_number = tk.Entry(self, width=3)
        self.input_number.focus()
        self.input_number.grid(row=1, column=4, padx=10)

        add_video_to_playlist_btn = tk.Button(self, text="Add Video To Playlist", command=self.add_video_to_playlist_clicked)
        add_video_to_playlist_btn.grid(row=2, column=3, columnspan=2, sticky="N", padx=10)

        playlist_name_lbl = tk.Label(self, text="Enter Playlist Name")
        playlist_name_lbl.grid(row=3, column=3, padx=10)

        self.input_name = tk.Entry(self, width=25)
        self.input_name.grid(row=4, column=3, columnspan=2, sticky="N", padx=10)

        self.status_lbl = tk.Label(self, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=5, column=0, columnspan=4, sticky="W", padx=10, pady=10)

    def set_text(self, text_area, content):
        text_area.insert(1.0, "\n")
        text_area.insert(1.0, content)

    def add_video_to_playlist_clicked(self):
        self.list_txt.config(state=NORMAL)
        key = self.input_number.get()
        name = lib.get_name(key)
        if name is not None:
            video = lib.get_info(key)
            self.__playlist.append(key)
            self.set_text(self.list_txt, f"{key} {video.info()}")
            self.list_txt.config(state=DISABLED)
        else:
            msb.showerror("Error", "Video not found")
        self.status_lbl.configure(text="Add Video To Playlist button was clicked!")

    def create_the_playlist_clicked(self):
        playlist_name = str(self.input_name.get()).strip()
        if len(self.__playlist) == 0:
            msb.showerror("Error", "Playlist is empty")

        elif playlist_name == '':
            msb.showerror("Error", "Playlist name is empty")

        elif playlist_name in self.__playlist_name:
            msb.showinfo("Playlist", "Playlist existed")
            
        else:
            msb.showinfo("Playlist", "Playlist created")
            with open('playlist.txt', 'a') as f:
                if os.path.getsize("playlist.txt") != 0: f.write("\n")
                f.write(f"Playlist: {playlist_name}")
                f.write("\n")
                for vid in self.__playlist:
                    f.write(f"{vid} {lib.get_info(vid).info()}\n")
                f.close()
            
            self.__playlist_name.append(playlist_name)
        self.status_lbl.configure(text="Create The Playlist button was clicked!")

    def reset_the_playlist_clicked(self):
        if len(self.__playlist) == 0:
            msb.showerror("Error", "Playlist is empty")
        else:
            self.list_txt.config(state=NORMAL)
            msb.showinfo("Playlist", "Reset playlist")
            self.__playlist.clear()
            self.list_txt.delete(1.0, tk.END)
            self.list_txt.config(state=DISABLED)
        self.status_lbl.configure(text="Reset The Playlist button was clicked!")