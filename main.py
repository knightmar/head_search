import io
import os.path
import random
import tkinter as tk
import urllib.request
from tkinter import messagebox
from tkinter.ttk import *

from PIL import ImageTk
from PIL import Image


class WebImage:
    def __init__(self, url):
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
        self.image = Image.open(io.BytesIO(raw_data))

    def get(self):
        return self.image


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.pseudo = ""
        self.head = None

        self.root = Frame(self).grid(padx=(100, 100), pady=(10, 10))

        self.entry = Entry(self.root, text="Pseudo")
        self.entry.grid(pady=(10, 10))

        self.confirm = Button(self.root, text="Confirm", command=self.confirm)
        self.confirm.grid(pady=(10, 10))

        self.saveBtn = Button(self.root, text="Save", command=self.save)
        self.saveBtn.grid(pady=(10, 10))
        self.saveBtn.configure(state=tk.DISABLED)

        fond = tk.PhotoImage(file='fond.png')
        self.imagelab = tk.Label(self, image=fond)
        self.imagelab.grid(pady=(0, 10))

    def confirm(self):
        self.pseudo = self.entry.get()
        self.url = "https://minotar.net/avatar/" + self.pseudo
        self.image = WebImage(self.url).get()
        self.head = ImageTk.PhotoImage(self.image)
        self.imagelab.configure(image=self.head)
        self.saveBtn.configure(state=tk.NORMAL)

    def save(self):
        filename = "head"
        if os.path.exists(filename + ".png"):
            rand = str(random.random())
            filename = filename + rand[2:5] + ".png"
        f = open(filename, "a")
        f.close()
        self.image.save(filename)
        messagebox.showinfo("Tout s'est bien passé", "L'image a bien été enregistré sous le nom de : " + filename)


if __name__ == "__main__":
    app = App()
    app.mainloop()
