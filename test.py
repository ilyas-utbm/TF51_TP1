import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os


def analyse(nom_fichier):
    a = np.loadtxt(nom_fichier, dtype=str, unpack=True)
    a = np.char.replace(a, ',', '.').astype(float)
    k = len(a)

    b = np.zeros(k)

    for i in range(1, k):
        b[i] = i * 0.001

    a = a.reshape(-1, 1)
    b = b.reshape(-1, 1)

    df = pd.DataFrame(b)

    df.columns = ['X']

    df['Y'] = a

    print(df)

    plt.plot(b[:k], a[:k], lw=0.1)
    plt.show()


analyse('mesure statique 45,1')
