import tkinter as tk
from tkinter import *
from video_library import lib
import tkinter.scrolledtext as tkst
from tkinter import messagebox as msb

class EditPlayVideosList(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.__playlist =  []
        self.__playlist_names = []

        tk.Label(self, text="Playlists").grid(row=0, column=0)
        tk.Label(self, text="Videos List").grid(row=0, column=1, columnspan=3)

        self.playlist_list_txt = Listbox(self, width=7, selectmode=SINGLE, exportselection=0)
        self.playlist_list_txt.grid(row=1, column=0, rowspan=5, sticky=W, padx=10, pady=10)
        self.playlist_list_txt.bind("<<ListboxSelect>>", self.__on_select)

        self.videos_list_txt = tkst.ScrolledText(self, width=40, height=12, wrap="none")
        self.videos_list_txt.grid(row=1, column=1, columnspan=3, rowspan=5, sticky=W, padx=10, pady=10)
        
        delete_the_playlist_btn = tk.Button(self, text="Delete Playlist", command=self.delete_playlist_clicked)
        delete_the_playlist_btn.grid(row=1, column=4, sticky=NW, pady=10)

        refresh_playlist_btn = tk.Button(self, text="Refresh Playlists", command=self.refresh_playlists_clicked)
        refresh_playlist_btn.grid(row=1, column=5, sticky=NW, pady=10, padx=10)

        play_playlist_btn = tk.Button(self, text="Play Playlist", command=self.play_playlist_clicked)
        play_playlist_btn.grid(row=1, column=6, sticky=NW, pady=10)

        add_lbl = tk.Label(self, text="Enter Video Number")
        add_lbl.grid(row=2, column=4, columnspan=2, sticky=W)

        self.add = tk.Entry(self, width=3)
        self.add.focus()
        self.add.grid(row=2, column=5)

        add_video_to_playlist_btn = tk.Button(self, text="Add Video To Playlist", command=self.add_video_to_playlist_clicked)
        add_video_to_playlist_btn.grid(row=3, column=4, columnspan=2, sticky=NW, padx=10)

        delete_lbl = tk.Label(self, text="Enter Video Number")
        delete_lbl.grid(row=4, column=4, columnspan=2, sticky=W)

        self.delete = tk.Entry(self, width=3)
        self.delete.grid(row=4, column=5)

        delete_video_from_playlist_btn = tk.Button(self, text="Delete Video From Playlist", command=self.delete_video_from_playlist_clicked)
        delete_video_from_playlist_btn.grid(row=5, column=4, columnspan=2, sticky=NW, padx=10)

        self.refresh_playlists_clicked()
        self.list_all_playlists()

    def set_text(self, text_area, content):
        text_area.insert(1.0, "\n")
        text_area.insert(1.0, content)

    def list_all_playlists(self):
        self.playlist_list_txt.delete(0, tk.END)
        for name in self.__playlist_names:
            self.playlist_list_txt.insert(tk.END, f"{name}\n")

    def __on_select(self, event):
        self.videos_list_txt.config(state=NORMAL)
        self.__playlist.clear()
        self.videos_list_txt.delete("1.0", tk.END)
        selected_index = self.playlist_list_txt.curselection()[0]
        playlist_name = self.__playlist_names[selected_index].strip()

        with open('playlist.txt', 'r') as f:
            lines = f.read().splitlines()
            for i in range(len(lines)):
                if lines[i].startswith("Playlist:") and str(lines[i].split(": ")[1].strip()) == playlist_name:
                    for j in range(i+1, len(lines)):
                        if lines[j] != "":
                            self.__playlist.append(f"{lines[j]}")
                        else: break

        self.set_text(self.videos_list_txt, "\n".join(self.__playlist))
        self.videos_list_txt.config(state=DISABLED)
                            
    def add_video_to_playlist_clicked(self):
        try:
            self.videos_list_txt.config(state=NORMAL)
            key = self.add.get()
            video_name = lib.get_name(key)
            selected_index = self.playlist_list_txt.curselection()[0]
            playlist_name = self.__playlist_names[selected_index].strip()

            if video_name is None:
                msb.showerror("Error", "Video not found")

            else:
                video = lib.get_info(key)
                self.__playlist.append(f"{key} {video.info()}")
                self.set_text(self.videos_list_txt, f"{key} {video.info()}")

                with open('playlist.txt', 'r') as f:
                    lines = f.readlines()
                    for i in range(len(lines)):
                        if lines[i].startswith("Playlist:") and str(lines[i].split(": ")[1].strip()) == playlist_name:
                            lines.insert(i+1, f"{key} {lib.get_info(key).info()}"  "\n")
                            with open('playlist.txt', 'w') as f:
                                f.writelines(lines)
                    f.close()

            self.videos_list_txt.config(state=DISABLED)

        except IndexError:
            msb.showerror("Error", "No playlist is selected")

    def delete_video_from_playlist_clicked(self):
        try:
            self.videos_list_txt.config(state=NORMAL)
            key = self.delete.get()
            video_name = lib.get_name(key)
            selected_index = self.playlist_list_txt.curselection()[0]
            playlist_name = self.__playlist_names[selected_index].strip()

            if video_name is None:
                msb.showerror("Error", "Video not found")

            elif len(self.__playlist) == 0:
                msb.showerror("Error", "Playlist empty")

            else:
                for vid in self.__playlist:
                    if vid.startswith(key):
                        self.__playlist.remove(vid)
                        break

                self.videos_list_txt.delete("1.0", tk.END)
                self.set_text(self.videos_list_txt, "\n".join(self.__playlist))

                with open('playlist.txt', 'r') as f:
                    lines = f.readlines()

                with open('playlist.txt', 'w') as f:
                    skip = False
                    key_deleted = False
                    for line in lines:
                        if line.startswith("Playlist:") and line.split(": ")[1].strip() == playlist_name:
                            f.write(line)
                            skip = True
                        elif skip and line.strip() == "":
                            skip = False
                            f.write(line)
                        elif skip and line.startswith(key):
                            if not key_deleted:
                                key_deleted = True
                                continue
                            else:
                                f.write(line)
                        else:
                            f.write(line)

            self.videos_list_txt.config(state=DISABLED)

        except IndexError:
            msb.showerror("Error", "No playlist is selected")

    def delete_playlist_clicked(self):
        try:
            self.videos_list_txt.config(state=NORMAL)
            selected_index = self.playlist_list_txt.curselection()[0]
            playlist_name = self.__playlist_names[selected_index].strip()
            
            self.__playlist.clear()
            self.videos_list_txt.delete("1.0", tk.END)
            
            with open('playlist.txt', 'r') as f:
                lines = f.readlines()

            with open('playlist.txt', 'w') as f:
                skip = False
                for line in lines:
                    if line.startswith("Playlist:") and line.split(": ")[1].strip() == playlist_name:
                        skip = True
                    elif skip and line.strip() == "":
                        skip = False
                        f.write(line)
                    elif skip:
                        continue
                    else:
                        f.write(line)
            
            self.videos_list_txt.config(state=DISABLED)
            self.__playlist_names.pop(selected_index)
            self.list_all_playlists()
        
        except IndexError:
            msb.showerror("Error", "No playlist is selected")

    def refresh_playlists_clicked(self):
        self.__playlist_names.clear()
        with open('playlist.txt', 'r') as f:
            lines = f.read().splitlines()
            for i in range(len(lines)):
                if lines[i].startswith("Playlist:"):
                    currentline = lines[i].split(": ")
                    name = str(currentline[1])
                    self.__playlist_names.append(name)
        self.list_all_playlists()

    def play_playlist_clicked(self):
        try:
            selected_index = self.playlist_list_txt.curselection()[0]
            playlist_name = self.__playlist_names[selected_index].strip()

            if len(self.__playlist) == 0:
                msb.showerror("Error", "Playlist is empty")
            else:
                for vid in self.__playlist:
                    lib.increment_play_count(vid.split(" ")[0])
                msb.showinfo("Play", "Playlist play")
        
        except IndexError:
            msb.showerror("Error", "No playlist is selected")