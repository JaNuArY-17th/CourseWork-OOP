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
        
        enter_lbl_1 = tk.Label(self, text="Enter Video Number")
        enter_lbl_1.grid(row=0, column=0, padx=10, pady=10)

        self.input_txt_number = tk.Entry(self, width=3)
        self.input_txt_number.focus()
        self.input_txt_number.grid(row=0, column=1, padx=10, pady=10)

        enter_lbl_2 = tk.Label(self, text="Enter Video New Rating")
        enter_lbl_2.grid(row=0, column=3, padx=10, pady=10)

        self.input_txt_rating = tk.Entry(self, width=3)
        self.input_txt_rating.grid(row=0, column=4, padx=10, pady=10)

        update_video_btn = tk.Button(self, text="Update Video", command=self.update_video_clicked)
        update_video_btn.grid(row=1, column=2, padx=10, pady=10)

        self.video_txt = tk.Text(self, width=50, height=5, wrap="none")
        self.video_txt.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        self.status_lbl = tk.Label(self, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)

    def set_text(self, text_area, content):
        text_area.delete("1.0", tk.END)
        text_area.insert(1.0, content)

    def update_video_clicked(self):
        try:
            self.video_txt.config(state=NORMAL)
            key = self.input_txt_number.get()
            rate = int(self.input_txt_rating.get())
            name = lib.get_name(key)
            if name is not None:
                video = lib.get_info(key)
                lib.set_rating(key, rate)
                self.set_text(self.video_txt, f"{key} {video.info()}")
                self.video_txt.config(state=DISABLED)
                msb.showinfo("Video", "Update video")
            else:
                msb.showerror("Error", "Video not found")
            self.status_lbl.configure(text="Update Video button was clicked!")
        except ValueError as err:
            msb.showerror("Error", err)
