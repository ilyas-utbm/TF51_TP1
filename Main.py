import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        # Définition de la taille et de la position de la fenêtre
        self.width = 400
        self.height = 30
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()
        self.x = (self.screen_width // 2) - (self.width // 2)
        self.y = (self.screen_height // 2) - (self.height // 2)
        self.master.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.z_label = tk.Label(self, text="Entrez la valeur de z:")
        self.z_label.pack(side="left")

        self.z_entry = tk.Entry(self)
        self.z_entry.pack(side="left")

        self.submit_button = tk.Button(self, text="Enregistrer", command=self.submit)
        self.submit_button.pack(side="left")

    def submit(self):
        z_value = self.z_entry.get()
        try:
            z_value = float(z_value.replace(',', '.'))
        except ValueError:
            # Si l'utilisateur a entré une valeur incorrecte, afficher un message d'erreur
            tk.messagebox.showerror("Erreur", "La valeur entrée pour z est incorrecte.")
            return

        # Si l'utilisateur a entré une valeur correcte, enregistrer la valeur de z
        self.z = z_value
        self.master.destroy()


def dynamique(nom_fichier):
    a, b = np.loadtxt(nom_fichier, dtype=str, unpack=True)
    b = np.char.replace(b, ',', '.').astype(float)
    a = np.char.replace(a, ',', '.').astype(float)
    k = len(a)
    wm = []
    af = np.zeros(k)
    aff = np.zeros(k)
    bf = np.zeros(k)
    bff = np.zeros(k)
    eta = np.zeros(k)
    af[0] = a[0]
    aff[0] = af[0]
    bf[0] = b[0]
    bff[0] = bf[0]

    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

    # Récupération de la valeur de z entrée par l'utilisateur
    z = app.z

    eta[0] = (bff[0] - 189.5) / (0.1 * z)

    for i in range(1, k):
        af[i] = 0.059 * a[i] + (1 - 0.059) * af[i - 1]
        aff[i] = 0.059 * af[i] + (1 - 0.059) * aff[i - 1]
        bf[i] = 0.059 * b[i] + (1 - 0.059) * bf[i - 1]
        bff[i] = 0.059 * bf[i] + (1 - 0.059) * bff[i - 1]
        eta[i] = (bff[i] - 189.5) / (0.1 * z)

        if round(b[i], 1) == 189.5:
            wm.append(aff[i])

    moyenne = sum(wm) / len(wm)
    resu = aff
    bl = bff
    eta

    tresu = resu.reshape(-1, 1)

    ble = bl.reshape(-1, 1)

    bexcel = b.reshape(-1, 1)

    aexcel = a.reshape(-1, 1)

    etae = eta.reshape(-1, 1)

    plt.plot(eta[:k], aff[:k] / moyenne, c='y', label='Profil des vitesses')
    plt.plot(eta[:k], 1 / (1 + 0.414 * (eta[:k] ** 2) ** 2), c='m', label='Prévision théorique')

    nom_fichier = os.path.basename(nom_fichier)
    plt.title("Profil des vitesses et prévision théorique en fonction de $\eta$ pour le fichier" + nom_fichier)
    plt.xlabel(r'$\eta$')
    plt.legend()
    plt.gcf().set_size_inches(15, 8)
    plt.savefig(nom_fichier + '.jpg', dpi=199)

    plt.show()

    df = pd.DataFrame(bexcel)

    df.columns = ['X']

    df['Y'] = aexcel

    df['X_lissé'] = ble

    df['Y_lissé'] = tresu

    df['eta'] = etae

    print(df)

    df.to_excel(nom_fichier + ' lissé.xlsx', index=False)


def statique(nom_fichier):
    a = np.loadtxt(nom_fichier, dtype=str, unpack=True)
    a = np.char.replace(a, ',', '.').astype(float)
    k = len(a)
    b = np.zeros(k)

    nom_fichier = os.path.basename(nom_fichier)

    for i in range(1, k):
        b[i] = i * 0.001

    a = a.reshape(-1, 1)
    b = b.reshape(-1, 1)

    df = pd.DataFrame(b)

    df.columns = ['X']

    df['Y'] = a

    print(df)

    df.to_excel(nom_fichier + '.xlsx', index=False)

    plt.plot(b[:k], a[:k], lw=0.1)
    plt.title('Vitesse du fluide en fonction du temps pour le fichier ' + nom_fichier)
    plt.xlabel('Temps en s')
    plt.ylabel('Vitesse du fluide en m/s')
    plt.gcf().set_size_inches(15, 8)
    plt.savefig(nom_fichier + '.jpg', dpi=199)
    plt.show()


# Définir la fonction qui sera appelée lorsque l'utilisateur fera un choix
def choix_utilisateur():
    global choix
    choix = var.get()
    fenetre.destroy()


# Créer la fenêtre et les widgets
fenetre = Tk()
var = StringVar()

# Obtenir la largeur et la hauteur de l'écran
largeur_ecran = fenetre.winfo_screenwidth()
hauteur_ecran = fenetre.winfo_screenheight()

# Calculer les coordonnées x et y pour centrer la fenêtre
x = (largeur_ecran - 170) // 2
y = (hauteur_ecran - 100) // 2

# Définir les coordonnées de la fenêtre
fenetre.geometry('170x100+{}+{}'.format(x, y))

titre = Label(fenetre, text='Choisir le type de mesure')
titre.pack()

option_a = Radiobutton(fenetre, text='Dynamique', variable=var, value="a")
option_a.pack()

option_b = Radiobutton(fenetre, text='Statique', variable=var, value="b")
option_b.pack()

bouton = Button(fenetre, text="Valider", command=choix_utilisateur)
bouton.pack()

# Afficher la fenêtre et attendre la réponse de l'utilisateur
fenetre.mainloop()

# Utiliser la réponse de l'utilisateur dans une condition if
if choix == "a":

    # Créer une fenêtre Tkinter
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    dynamique(file_path)

    pass
elif choix == "b":

    # Créer une fenêtre Tkinter
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    statique(file_path)

    pass
else:
    # Gérer le cas où l'utilisateur n'a pas choisi une option valide
    pass
