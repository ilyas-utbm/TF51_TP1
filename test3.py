import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        # Définition de la taille et de la position de la fenêtre
        self.width = 300
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


root = tk.Tk()
app = Application(master=root)
app.mainloop()

# Récupération de la valeur de z entrée par l'utilisateur
z = app.z
print("La valeur de z est :", z)
