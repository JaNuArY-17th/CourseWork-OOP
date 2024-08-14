import tkinter as tk
from tkinter import *
from tkinter import ttk
from video_library import lib
from episode_library import ep_lib
import font_manager as fonts
import tkinter.scrolledtext as tkst
from tkinter import messagebox as msb
import os

class VideoEpisodes(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.episodes = []
        self.videos = []

        tk.Label(self, text="Videos").grid(row=0, column=0)
        tk.Label(self, text="Episodes").grid(row=0, column=1)

        self.videos_list = Listbox(self, width=40, selectmode=SINGLE, exportselection=0)
        self.videos_list.grid(row=1, column=0, rowspan=5, padx=10, pady=10)
        self.videos_list.bind("<<ListboxSelect>>", self.__on_select)

        self.episodes_list = Listbox(self, width=20, selectmode=SINGLE, exportselection=0)
        self.episodes_list.grid(row=1, column=1, rowspan=5, padx=10, pady=10)

        list_videos_btn = tk.Button(self, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=6, column=0)

        self.list_videos_clicked()


    def set_text(self, text_area, content):
        text_area.delete(0, tk.END)
        lines = content.split('\n')
        for line in lines:
            text_area.insert(tk.END, f"{line}\n")

    def __on_select(self, event):
        self.episodes.clear()
        self.episodes_list.delete(0, tk.END)
        selected_index = self.videos_list.curselection()[0]
        video = self.videos[selected_index].strip()

        with open('episode.txt','r') as f:
            lines = f.read().splitlines()
            for line in lines:
                if line.split(',')[0].strip() == video.strip():
                    self.episodes.append(f'Episode {line.split(',')[-1]}')

        self.set_text(self.episodes_list, '\n'.join(self.episodes))                  

    def list_videos_clicked(self):
        video_list = lib.list_all()
        lines = video_list.split('\n')
        self.videos_list.delete(0, tk.END)
        for line in lines:
            self.videos_list.insert(tk.END, f"{line}\n")
            key = line.split(' ')[0]
            name = lib.get_name(key)
            if name is not None:
                self.videos.append((name))