import tkinter as tk
from tkinter import ttk

class ScrollableNotebook(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        # Create a canvas to hold the notebook
        self.canvas = tk.Canvas(self, borderwidth=0)
        self.frame = ttk.Frame(self.canvas)
        self.scrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=self.scrollbar.set)

        # Place the scrollbar and canvas
        self.scrollbar.pack(side="bottom", fill="x", expand=False)
        self.canvas.pack(side="top", fill="both", expand=True)

        # Create a window inside the canvas to place the frame
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        # Initialize the notebook inside the frame
        self.notebook = ttk.Notebook(self.frame)
        self.notebook.pack(side="left", fill="both", expand=True)

        # Bind the resizing event to adjust the canvas size
        self.frame.bind("<Configure>", self.on_frame_configure)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def add(self, child, **kwargs):
        self.notebook.add(child, **kwargs)

    def tab(self, *args, **kwargs):
        return self.notebook.tab(*args, **kwargs)

# Example usage
root = tk.Tk()
root.geometry("400x300")

scrollable_notebook = ScrollableNotebook(root)
scrollable_notebook.pack(fill="both", expand=True)

# Add tabs to the scrollable notebook
for i in range(10):
    frame = ttk.Frame(scrollable_notebook.notebook)
    ttk.Label(frame, text=f"Tab {i+1} content").pack(padx=10, pady=10)
    scrollable_notebook.add(frame, text=f"Tab {i+1}")

root.mainloop()
