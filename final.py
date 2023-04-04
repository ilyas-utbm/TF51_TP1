# Demander à l'opérateur de selectionner les fichiers
# Pour chaque fichier : Demander z
#                       Lisser les courbes
#                       Calculer w/wm
#                       Calculer théorie
#                       Enregistrer dans un excel les données
#                       Afficher toutes les courbes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os


def dynamique(nom_fichier, centre, couleur, z, p):
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

    eta[0] = (bff[0] - centre) / (0.1 * z)

    for i in range(1, k):
        af[i] = 0.059 * a[i] + (1 - 0.059) * af[i - 1]
        aff[i] = 0.059 * af[i] + (1 - 0.059) * aff[i - 1]
        bf[i] = 0.059 * b[i] + (1 - 0.059) * bf[i - 1]
        bff[i] = 0.059 * bf[i] + (1 - 0.059) * bff[i - 1]
        eta[i] = (bff[i] - centre) / (0.1 * z)

        if round(b[i], 1) == 189.5:
            wm.append(aff[i])

    moyenne = sum(wm) / len(wm)
    resu = aff
    bl = bff

    profil = aff[:k] / moyenne

    theorie = 1 / (1 + 0.414 * (eta[:k] ** 2) ** 2)

    tresu = resu.reshape(-1, 1)

    ble = bl.reshape(-1, 1)

    bexcel = b.reshape(-1, 1)

    aexcel = a.reshape(-1, 1)

    etae = eta.reshape(-1, 1)

    profil_e = profil.reshape(-1, 1)
    theorie_e = theorie.reshape(-1, 1)

    if p == 0:
        plt.plot(eta[:k], theorie, c='k', label='Prévision théorique')

    plt.plot(eta[:k], profil, c=couleur, label='Profil des vitesses pour z = ' + str(z))

    df = pd.DataFrame(bexcel)

    df.columns = ['X']

    df['Y'] = aexcel

    df['X_lissé'] = ble

    df['Y_lissé'] = tresu

    df['eta'] = etae

    df['profil'] = profil_e

    df['theorie'] = theorie_e

    df.to_excel(nom_fichier + ' lissé.xlsx', index=False)


nom_fichier = ['mesure 30,1mm', 'mesure 40,1mm', 'mesure 50,1mm', 'mesure 60,1mm', 'mesure 70,1mm']

z = [30.1, 40.1, 50.1, 60.1, 70.1]

couleur = ['b', 'g', 'r', 'c', 'y']

centre = 189.5

i = len(nom_fichier)

for k in range(0, i):
    dynamique(nom_fichier[k], centre, couleur[k], z[k], k)


ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.title("Profil des vitesses et prévision théorique en fonction de $\eta$ pour le fichier")
plt.xlabel(r'$\eta$')
plt.legend()
plt.gcf().set_size_inches(15, 8)
plt.savefig('final.jpg', dpi=199)
plt.show()
