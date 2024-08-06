import tkinter as tk
from tkinter import *
from video_library import lib
from tkinter import messagebox as msb

class EditLibrary(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        tk.Label(self, text="Add New Video").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        tk.Label(self, text="Delete Video").grid(row=0, column=2, columnspan=2, padx=10, pady=10)

        lbl_name = tk.Label(self, text="Name: ")
        lbl_name.grid(row=1, column=0, padx=10, pady=10)

        self.name = tk.Entry(self, width=30)
        self.name.focus()
        self.name.grid(row=1, column=1, padx=10, pady=10)

        lbl_director = tk.Label(self, text="Director: ")
        lbl_director.grid(row=2, column=0, padx=10, pady=10)

        self.director = tk.Entry(self, width=30)
        self.director.grid(row=2, column=1, padx=10, pady=10)

        lbl_rating = tk.Label(self, text="Rating: ")
        lbl_rating.grid(row=3, column=0, padx=10, pady=10)

        self.rating = tk.Entry(self, width=30)
        self.rating.grid(row=3, column=1, padx=10, pady=10)

        lbl_image_path = tk.Label(self, text="Image Path: ")
        lbl_image_path.grid(row=4, column=0, padx=10, pady=10)

        self.image_path = tk.Entry(self, width=30)
        self.image_path.grid(row=4, column=1, padx=10, pady=10)

        add_btn = tk.Button(self, text="Add Video", command=self.add_video_clicked)
        add_btn.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.videos_list_txt = Listbox(self, width=40, selectmode=SINGLE, exportselection=0)
        self.videos_list_txt.grid(row=1, column=2, rowspan=4, padx=10, pady=10)
        self.videos_list_txt.bind("<<ListboxSelect>>", self.__on_select)

        delete_btn = tk.Button(self, text="Delete Video", command=self.delete_video_clicked)
        delete_btn.grid(row=5, column=2, columnspan=2, padx=10, pady=10)

        self.list_videos()
    
    def set_text(self, text_area, content):
        text_area.delete(0, tk.END)
        lines = content.split('\n')
        for line in lines:
            text_area.insert(tk.END, f"{line}\n")

    def __on_select(self, event):
        selected_index = self.videos_list_txt.curselection()[0]

    def add_video_clicked(self):
        try:
            name = self.name.get()
            director = self.director.get()
            rating = self.rating.get()
            image_path = self.image_path.get()

            lib.add_video_to_library(name, director, int(rating), image_path)
            msb.showinfo("Add Video", "Add Video succesfull")

            self.list_videos()
        except ValueError as err:
            msb.showerror("Error", err)

    def list_videos(self):
        video_list = lib.list_all()
        self.set_text(self.videos_list_txt, video_list)

    def delete_video_clicked(self):
        selected_index = self.videos_list_txt.curselection()[0]
        video_str = self.videos_list_txt.get(selected_index)
        current_video_key = video_str.split(" ")[0]
        lib.delete_video_from_library(current_video_key)
        self.list_videos()
