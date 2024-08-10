# Import necessary modules
import tkinter as tk
from tkinter import *
from video_library import lib
from PIL import Image, ImageTk

# Define the CheckVideos class that inherits from tkinter.Frame
class CheckVideos(Frame):
    def __init__(self, master):
        # Call the constructor of the parent class
        Frame.__init__(self, master)

        # Create a button that triggers the list_videos_clicked method when clicked
        list_videos_btn = tk.Button(self, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        # Create a label for displaying video information
        tk.Label(self, text="Video Info").grid(row=0, column=3)

        # Create a listbox for displaying video
        self.videos_list_txt = Listbox(self, width=48, height=15, selectmode=SINGLE, exportselection=0)
        self.videos_list_txt.grid(row=1, column=0, columnspan=3, sticky=W, padx=10)
        # Bind the __on_select method to the ListboxSelect event
        self.videos_list_txt.bind("<<ListboxSelect>>", self.__on_select)

        # Create a text area for displaying video details
        self.video_txt = Text(self, width=30, height=4)
        self.video_txt.grid(row=1, column=3, sticky=NW, padx=10)

        # Create a label for displaying video images
        self.video_image_label = Label(self)
        self.video_image_label.grid(row=1, column=3, rowspan=2, padx=10, sticky=SW)

        # Call the list_videos_clicked method to populate the listbox with video 
        self.list_videos_clicked()

    # Method to set the text of a text area
    def set_text(self, text_area, content):
        # delete the existing content of the text area
        text_area.delete("1.0", tk.END)
        # Insert the new content into the text area
        text_area.insert(1.0, content)

    # Method to handle the ListboxSelect event
    def __on_select(self, event):
        # Get the selected index from the listbox
        selected_index = self.videos_list_txt.curselection()[0]
        # Get the video from the listbox
        video_str = self.videos_list_txt.get(selected_index)
        # Extract the video key from the video 
        key = video_str.split(" ")[0]
        
        # Enable the text area for editing
        self.video_txt.config(state=NORMAL)
        # Get video details from the library
        name = lib.get_name(key)
        if name is not None:
            # Get the video director from the library
            director = lib.get_director(key)
            # Get the rating from the library
            rating = lib.get_rating(key)
            # Get the play count from the library
            play_count = lib.get_play_count(key)
            # Format the video details
            video_details = f"Name: {name}\nDirector: {director}\nRating: {rating}\nPlays: {play_count}"
            # Set the video details in the text area
            self.set_text(self.video_txt, video_details)
        else:
            # Set an error message in the text area if the video is not found
            self.set_text(self.video_txt, f"Video not found")
        # Disable the text area after editing
        self.video_txt.config(state=DISABLED)

        # Update the video image in the label
        self.update_video_image(key)

    # Method to update the video image in the label
    def update_video_image(self, key):
        # Get the image path from the library
        image_path = lib.get_image_path(key)

        try:
            # Open the image file
            image = Image.open(image_path)
            # Resize the image to a thumbnail
            image.thumbnail((300, 300))
            # Convert the image to a PhotoImage object
            photo = ImageTk.PhotoImage(image)

            # Set the PhotoImage object as the image of the label
            self.video_image_label.config(image=photo)
            # Keep a reference to the PhotoImage object to avoid garbage collection
            self.video_image_label.image = photo  
        except Exception as e:
            # Set an error message in the label if the image is not available
            self.video_image_label.config(image='', text='Image not available')

    # Method to populate the listbox with video 
    def list_videos_clicked(self):
        # Get the list of video from the library
        video_list = lib.list_all()
        # Split the video into lines
        lines = video_list.split('\n')
        # Clear the listbox
        self.videos_list_txt.delete(0, tk.END)
        # Add the video  to the listbox
        for line in lines:
            self.videos_list_txt.insert(tk.END, f"{line}\n")