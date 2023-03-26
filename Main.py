import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os


def dynamique(nom_fichier):
    a, b = np.loadtxt(nom_fichier, dtype=str, unpack=True)
    b = np.char.replace(b, ',', '.').astype(float)
    a = np.char.replace(a, ',', '.').astype(float)
    k = len(a)
    af = np.zeros(k)
    aff = np.zeros(k)
    af[0] = a[0]
    aff[0] = af[0]
    for i in range(1, k):
        af[i] = 0.059 * a[i] + (1 - 0.059) * af[i - 1]
        aff[i] = 0.059 * af[i] + (1 - 0.059) * aff[i - 1]

    resu = aff
    tresu = resu.reshape(-1, 1)

    bexcel = b.reshape(-1, 1)

    aexcel = a.reshape(-1, 1)

    plt.scatter(b[:k], a[:k], c='y', s=1, label='Données non lissées')
    plt.scatter(b[:k], aff[:k], c='m', s=1, label='Données lissées')
    nom_fichier = os.path.basename(nom_fichier)
    plt.title('Vitesse du fluide en fonction du déplacement de la sonde pour le fichier ' + nom_fichier)
    plt.xlabel('Déplacement de la sonde en mm')
    plt.ylabel('Vitesse du fluide en m/s')
    plt.legend()
    plt.gcf().set_size_inches(15, 8)
    plt.savefig(nom_fichier + '.jpg', dpi=199)
    plt.show()

    df = pd.DataFrame(bexcel)

    df.columns = ['X']

    df['Y_lissé'] = tresu

    df['Y'] = aexcel

    print(df)

    df.to_excel(nom_fichier + ' lissé.xlsx', index=False)

    # Ajouter courbe de tendance et son equation y=x


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
