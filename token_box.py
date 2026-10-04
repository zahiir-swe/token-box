import tkinter as tk
from tkinter import simpledialog, messagebox
import keyboard
import keyring
import pyperclip
import json
import os
import sys

# Ce fichier stockera uniquement les NOMS des tokens. 
# Les vrais secrets sont dans le trousseau chiffré de l'OS.
CONFIG_FILE = os.path.expanduser("~/.token_box.json")
SERVICE_NAME = "DevTokenBox"

class TokenBox:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Boîte à Tokens")
        self.root.geometry("350x450")
        self.root.attributes("-topmost", True) # Toujours au premier plan
        self.root.protocol("WM_DELETE_WINDOW", self.hide_window)
        self.root.withdraw() # Démarrer en mode masqué en arrière-plan

        self.keys = self.load_keys()
        self.build_ui()
        
        # Le fameux raccourci global
        keyboard.add_hotkey('ctrl+shift+o', self.show_window)

    def build_ui(self):
        tk.Label(self.root, text="Boîte à Tokens", font=("Helvetica", 14, "bold")).pack(pady=10)

        self.listbox = tk.Listbox(self.root, font=("Consolas", 12), selectbackground="#0078D7")
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)
        # Double clic pour copier
        self.listbox.bind('<Double-Button-1>', lambda e: self.copy_token())

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Copier", width=8, command=self.copy_token).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Ajouter", width=8, command=self.add_token).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Supprimer", width=8, command=self.delete_token).pack(side=tk.LEFT, padx=5)

        tk.Label(self.root, text="Fermez pour masquer.\nCTRL+SHIFT+O pour rouvrir.", font=("Helvetica", 8), fg="gray").pack(pady=5)
        self.update_listbox()

    def load_keys(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        return []

    def save_keys(self):
        with open(CONFIG_FILE, 'w') as f:
            json.dump(self.keys, f)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for k in self.keys:
            self.listbox.insert(tk.END, k)

    def show_window(self):
        self.root.deiconify()
        self.root.focus_force()

    def hide_window(self):
        self.root.withdraw()

    def copy_token(self):
        selection = self.listbox.curselection()
        if not selection:
            return
        key_name = self.listbox.get(selection[0])
        token = keyring.get_password(SERVICE_NAME, key_name)
        
        if token:
            pyperclip.copy(token)
            self.hide_window() # Masque l'interface dès que c'est copié, prêt à coller !

    def add_token(self):
        name = simpledialog.askstring("Nouveau", "Nom du token (ex: Github_Perso) :", parent=self.root)
        if not name: return
        token = simpledialog.askstring("Nouveau", f"Collez le token pour {name} :", parent=self.root)
        if not token: return

        keyring.set_password(SERVICE_NAME, name, token)
        if name not in self.keys:
            self.keys.append(name)
            self.save_keys()
        self.update_listbox()

    def delete_token(self):
        selection = self.listbox.curselection()
        if not selection: return
        key_name = self.listbox.get(selection[0])
        
        if messagebox.askyesno("Supprimer", f"Supprimer le token '{key_name}' ?", parent=self.root):
            try:
                keyring.delete_password(SERVICE_NAME, key_name)
            except Exception:
                pass
            self.keys.remove(key_name)
            self.save_keys()
            self.update_listbox()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TokenBox()
    app.run()