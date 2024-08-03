import tkinter as tk
from tkinter import *
from tkinter import ttk
from video_library import lib
import font_manager as fonts
import tkinter.scrolledtext as tkst
from tkinter import messagebox as msb
import os

class CheckVideos(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        list_videos_btn = tk.Button(self, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(self, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(self, width=3)
        self.input_txt.focus()
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_video_btn = tk.Button(self, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(self, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_txt = tk.Text(self, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(self, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_videos_clicked()

    def set_text(self, text_area, content):
        text_area.delete("1.0", tk.END)
        text_area.insert(1.0, content)

    def check_video_clicked(self):
        self.video_txt.config(state=NORMAL)
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            self.set_text(self.video_txt, video_details)
            self.video_txt.config(state=DISABLED)
        else:
            self.set_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")

    def list_videos_clicked(self):
        self.list_txt.config(state=NORMAL)
        video_list = lib.list_all()
        self.set_text(self.list_txt, video_list)
        self.list_txt.config(state=DISABLED)
        self.status_lbl.configure(text="List Videos button was clicked!")
