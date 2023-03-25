from tkinter import *

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
x = (largeur_ecran - 300) // 2
y = (hauteur_ecran - 150) // 2

# Définir les coordonnées de la fenêtre
fenetre.geometry('300x150+{}+{}'.format(x, y))

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
    # Faire quelque chose pour l'option a
    pass
elif choix == "b":
    # Faire quelque chose pour l'option b
    pass
else:
    # Gérer le cas où l'utilisateur n'a pas choisi une option valide
    pass