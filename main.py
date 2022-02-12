import io
import tkinter as tk
import urllib.request
from tkinter import ttk

from PIL import ImageTk, Image


class WebImage:
    def __init__(self, url):
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
        image = Image.open(io.BytesIO(raw_data))
        self.image = ImageTk.PhotoImage(image)

    def get(self):
        return self.image


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.pseudo = ""
        self.head = None

        self.entry = ttk.Entry(self, text="Pseudo")
        self.entry.pack()
        self.confirm = ttk.Button(self, text="Confirm", command=self.confirm)
        self.confirm.pack()

    def confirm(self):
        self.pseudo = self.entry.get()
        self.url = "https://minotar.net/avatar/" + self.pseudo
        self.head = WebImage(self.url).get()
        self.imagelab = tk.Label(self, image=self.head)
        self.imagelab.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()


    def get(self):
        return self.image
