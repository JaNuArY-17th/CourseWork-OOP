import tkinter as tk
from tkinter import *
from tkinter import ttk
from video_library import lib
import font_manager as fonts
import tkinter.scrolledtext as tkst
from tkinter import messagebox as msb
import os

class UpdateVideos(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        list_videos_btn = tk.Button(self, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        self.videos_list_txt = Listbox(self, width=48, height=12, selectmode=SINGLE, exportselection=0)
        self.videos_list_txt.grid(row=1, column=0, columnspan=3, rowspan=10, sticky=W, padx=10)
        self.videos_list_txt.bind("<<ListboxSelect>>", self.__on_select)
        
        enter_lbl_1 = tk.Label(self, text="Enter Video Number")
        enter_lbl_1.grid(row=1, column=3, padx=10, pady=10, sticky=NW)

        self.input_txt_number = tk.Entry(self, width=3)
        self.input_txt_number.focus()
        self.input_txt_number.grid(row=1, column=4, padx=10, pady=10, sticky=NW)

        enter_lbl_2 = tk.Label(self, text="Enter Video New Rating")
        enter_lbl_2.grid(row=2, column=3, padx=10, pady=10, sticky=NW)

        self.input_txt_rating = tk.Entry(self, width=3)
        self.input_txt_rating.grid(row=2, column=4, padx=10, pady=10, sticky=NW)

        update_video_btn = tk.Button(self, text="Update Video", command=self.update_video_clicked)
        update_video_btn.grid(row=3, column=3, columnspan=2, padx=10, pady=10)

        self.video_txt = tk.Text(self, width=30, height=5, wrap="none")
        self.video_txt.grid(row=4, column=3, columnspan=2, padx=10, pady=10)

        self.list_videos_clicked()

    def set_text(self, text_area, content):
        text_area.delete("1.0", tk.END)
        text_area.insert(1.0, content)

    def update_video_clicked(self):
        try:
            self.video_txt.config(state=NORMAL)
            key = self.input_txt_number.get()
            if key.strip() == "":
                selected_index = self.videos_list_txt.curselection()[0]
                video = self.videos_list_txt.get(selected_index).split(" ")[0]

                rate = int(self.input_txt_rating.get())
                lib.set_rating(video, rate)
                self.display_video_info(video, lib.get_name(video))
                self.list_videos_clicked()
                self.video_txt.config(state=DISABLED)
                msb.showinfo("Video", "Update video")

            else:
                rate = int(self.input_txt_rating.get())
                name = lib.get_name(key)

                if name is not None:
                    lib.set_rating(key, rate)
                    self.display_video_info(key, name)
                    self.video_txt.config(state=DISABLED)
                    msb.showinfo("Video", "Update video")
                else:
                    msb.showerror("Error", "Video not found")
        except ValueError as err:
            msb.showerror("Error", err)

    def list_videos_clicked(self):
        video_list = lib.list_all()
        lines = video_list.split('\n')
        self.videos_list_txt.delete(0, tk.END)
        for line in lines:
            self.videos_list_txt.insert(tk.END, f"{line}\n")

    def display_video_info(self, key, name):
        director = lib.get_director(key)
        rating = lib.get_rating(key)
        play_count = lib.get_play_count(key)
        video_details = f"Name: {name}\nDirector: {director}\nRating: {rating}\nPlays: {play_count}"
        self.set_text(self.video_txt, video_details)

    def __on_select(self, event):
        selected_index = self.videos_list_txt.curselection()[0]
        video_str = self.videos_list_txt.get(selected_index)
        key = video_str.split(" ")[0]
        
        self.video_txt.config(state=NORMAL)
        name = lib.get_name(key)
        if name is not None:
            self.display_video_info(key, name)
        else:
            self.set_text(self.video_txt, f"Video not found")
        self.video_txt.config(state=DISABLED)
