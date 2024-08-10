import tkinter as tk
from tkinter import *
from tkinter import ttk
import font_manager as fonts
from tab_check_videos import CheckVideos
from tab_create_videos_list import CreateVideosList
from tab_update_videos import UpdateVideos
from tab_search import Search
from tab_edit_library import EditLibrary
from tab_edit_play_videos_list import EditPlayVideosList

import subprocess
import sys

# Root class to create the interface and define the controller function to switch frames
class RootApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(NoteBook)

    # controller function
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def reset_program(self):
        self.destroy()
        subprocess.Popen([sys.executable] + sys.argv)
        sys.exit()

# sub-root to contain the Notebook frame and a controller function to switch the tabs within the notebook
class NoteBook(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.notebook = ttk.Notebook()
        self.tab1 = CheckVideos(self.notebook)
        self.tab2 = CreateVideosList(self.notebook)
        self.tab3 = EditPlayVideosList(self.notebook)
        self.tab5 = UpdateVideos(self.notebook)
        self.tab6 = Search(self.notebook)
        self.tab7 = EditLibrary(self.notebook)

        self.notebook.add(self.tab1, text="Check Videos")
        self.notebook.add(self.tab2, text="Create Videos List")
        self.notebook.add(self.tab3, text="Edit/Play Videos List")
        self.notebook.add(self.tab5, text="Update Videos")
        self.notebook.add(self.tab6, text="Search")
        self.notebook.add(self.tab7, text="Edit Library")

        self.notebook.pack()

        reset_btn = tk.Button(self, text="Refresh", command=self.master.reset_program).grid(row=1, column=1)


if __name__ == "__main__":
    Root = RootApp()
    fonts.configure()
    Root.geometry("850x450")
    Root.title("Video Player")
    style = ttk.Style()
    style.configure("TNotebook.Tab", padding=[10, 5])
    Root.mainloop()
