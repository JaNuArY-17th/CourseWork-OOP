import tkinter as tk
from tkinter import *
from tkinter import ttk
from video_library import lib
import font_manager as fonts
import tkinter.scrolledtext as tkst
from tkinter import messagebox as msb
import os

class Search(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        enter_lbl = tk.Label(self, text="Search by")
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        global category
        category = ttk.Combobox(self, values=('Video', 'Director', 'Rating'), width=10, textvariable=tk.StringVar)
        category.grid(row=0, column=1, sticky="W")
        category.current(0)

        self.input_txt = tk.Entry(self, width=20)
        self.input_txt.focus()
        self.input_txt.grid(row=1, column=0)

        search_btn = tk.Button(self, text="Search", command=self.search)
        search_btn.grid(row=1, column=1, sticky="W")

        self.result_txt = tk.Text(self, width=50, height=10, wrap="none")
        self.result_txt.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def set_text(self, text_area, content):
        text_area.insert(1.0, "\n")
        text_area.insert(1.0, content)

    def get_current_item(self):
        return category.current()

    def search(self):
        self.result_txt.config(state=NORMAL)
        self.result_txt.delete("1.0", tk.END)
        key = self.input_txt.get()
        if self.get_current_item() == 0:
            for vid in lib.library.values():
                if key.lower() in vid.name.lower() and key.isalpha() == True:
                    self.set_text(self.result_txt, vid.info())
        elif self.get_current_item() == 1:
            for direc in lib.library.values():
                if key.lower() in direc.director.lower() and key.isalpha() == True:
                    self.set_text(self.result_txt, direc.info())
        else:
            for rate in lib.library.values():
                if int(key) == rate.rating:
                    self.set_text(self.result_txt, rate.info())
        self.result_txt.config(state=DISABLED)