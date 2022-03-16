import io
import os.path
import random
import sys
import tkinter as tk
import urllib.request
from tkinter import messagebox
from tkinter.ttk import *
import subprocess

from PIL import ImageTk
from PIL import Image

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def connect():
    try:
        urllib.request.urlopen('https://minotar.net/')  # Python 3.x
        return True
    except:
        return False


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
        self.iconbitmap(resource_path("./img/icon.ico"))
        self.wm_title("Head Searcher")

        self.root = Frame(self).grid(padx=100, pady=10)

        self.resizable(0, 0)

        Label(self.root, text="Head Searcher").grid()

        # champ pseudo
        Label(self.root, text="Pseudo :").grid()

        self.entry = Entry(self.root)
        self.entry.grid(pady=(1, 10))

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

        self.openBtn = Button(self.root, text="Ouvrir le dossier des images", command=self.showImg)
        self.openBtn.grid()

        # label image
        fond = tk.PhotoImage(file=resource_path("./img/fond.png"))
        self.imagelab = tk.Label(self, image=fond)
        self.imagelab.grid(pady=(0, 10))

        Label(self.root, text="knightmar - All rights reserved").grid()

    # fnc appellée au clic du bouton confirm
    def confirm(self):
        self.pseudo = self.entry.get()
        self.url = "https://minotar.net/" + str(self.radio()) + "/" + self.pseudo
        self.image = WebImage(self.url).get()
        self.head = ImageTk.PhotoImage(self.image)
        self.imagelab.configure(image=self.head)
        self.saveBtn.configure(state=tk.NORMAL)

    # fnc qui permet de sav l'image dans un fichier
    def save(self):
        filename = self.pseudo + " - " + self.radio()
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

    def showImg(self):
        subprocess.Popen(r'explorer /open,".\sortie_images"')


if __name__ == "__main__":
    #if os.path.exists("./img"):
        if connect():
            app = App()
            app.mainloop()
        else:
            messagebox.showerror("Serveur non trouvé",
                                 "votre connexion ne vous permets pas d'utiliser cette application, demandez a un adminstrateur réseau, ou utilisez un VPN.")

    #else:
       # messagebox.showerror("Dossier requis non trouvé",
        #                     "Un dossier nécéssaire au bon fonctionnement du logiciel (img) n'a pas été trouvé.\nVeuillez ne pas le séparer de cet éxecutable")
