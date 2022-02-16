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
        # Variables
        self.pseudo = ""
        self.head = None
        self.radioVar = tk.IntVar(value=1)
        self.iconbitmap("icon.ico")

        self.root = Frame(self).grid(padx=100, pady=10)

        self.resizable(0, 0)

        # champ pseudo
        self.pseudo_label = Label(self.root, text="Pseudo :").grid()

        self.entry = Entry(self.root)
        self.entry.grid(pady=(10, 10))

        # champs radio buttons
        self.tete = Radiobutton(self.root, text="Tête", variable=self.radioVar, value=1)
        self.tete.grid()

        self.helmet = Radiobutton(self.root, text="Tête + Châpeau", variable=self.radioVar, value=2)
        self.helmet.grid()

        self.isometric = Radiobutton(self.root, text="Tête isométrique", variable=self.radioVar, value=3)
        self.isometric.grid()

        self.body = Radiobutton(self.root, text="Corps", variable=self.radioVar, value=4)
        self.body.grid()

        self.bust = Radiobutton(self.root, text="Buste", variable=self.radioVar, value=5)
        self.bust.grid()

        self.skin = Radiobutton(self.root, text="Skin", variable=self.radioVar, value=6)
        self.skin.grid()

        # boutons confirm + save
        self.confirm = Button(self.root, text="Confirm", command=self.confirm)
        self.confirm.grid(pady=(10, 10))

        self.saveBtn = Button(self.root, text="Save", command=self.save)
        self.saveBtn.grid(pady=(10, 10))
        self.saveBtn.configure(state=tk.DISABLED)

        # label image
        fond = tk.PhotoImage(file='fond.png')
        self.imagelab = tk.Label(self, image=fond)
        self.imagelab.grid(pady=(0, 10))

    # fnc appellée au clic du bouton confirm
    def confirm(self):
        self.pseudo = self.entry.get()
        self.url = "https://minotar.net/" + str(self.radio()) + "/" + self.pseudo
        print(self.url)
        self.image = WebImage(self.url).get()
        self.head = ImageTk.PhotoImage(self.image)
        self.imagelab.configure(image=self.head)
        self.saveBtn.configure(state=tk.NORMAL)

    # fnc qui permet de sav l'image dans un fichier
    def save(self):
        filename = "skin"
        if not os.path.exists("./sortie_images"):
            os.mkdir("./sortie_images")
        if os.path.exists("./sortie_images/" + filename + ".png"):
            nb = str(random.random())
            filename = filename + nb[2:5] + ".png"
        else:
            filename = filename + ".png"
        f = open("./sortie_images/" + filename, "a")
        f.close()
        self.image.save("./sortie_images/" + filename)
        messagebox.showinfo("Tout s'est bien passé", "L'image a bien été enregistré sous le nom de : " + filename)

    # fnc appellé pour récup les radios buttons
    def radio(self):
        if self.radioVar.get() == 1:
            return "avatar"
        if self.radioVar.get() == 2:
            return "helm"
        if self.radioVar.get() == 3:
            return "cube"
        if self.radioVar.get() == 4:
            return "body"
        if self.radioVar.get() == 5:
            return "bust"
        if self.radioVar.get() == 6:
            return "skin"


if __name__ == "__main__":
    app = App()
    app.mainloop()
