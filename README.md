# 🔑 TokenBox

Une "boîte à tokens" ultra-légère et locale pour les développeurs Windows. Accessible en 1 seconde via un raccourci global (`CTRL + SHIFT + O`), vos jetons (GitHub, Hugging Face, clés API...) sont immédiatement copiés dans votre presse-papier sans jongler entre plusieurs onglets.

Les secrets sont chiffrés et stockés dans le trousseau natif de votre système d'exploitation (**Windows Credential Manager**).

---

## ⚡ Fonctionnalités

- **Raccourci global** : Ouvrez et masquez l'interface avec `CTRL + SHIFT + O`.
- **Copie rapide** : Double-cliquez sur n'importe quel token pour le copier et masquer la fenêtre automatiquement.
- **Sécurité native** : Les valeurs des clés sont stockées via `keyring` dans le gestionnaire d'identifiants Windows. Seuls les noms des tokens sont sauvegardés localement (`~/.token_box.json`).
- **Léger & Silencieux** : ~20 Mo de RAM, aucun impact CPU, tourne en tâche de fond.

---

## 🛠️ Installation

### Prérequis
- Windows 10/11
- Python 3.x installé

### Procédure rapide
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-user/token-box.git
   cd token-box
   ```

2. Lancez le script d'installation :
   - Double-cliquez sur `install.bat`.
   - Ce script va installer les dépendances Python (`keyring`, `keyboard`, `pyperclip`, `pyinstaller`), compiler l'exécutable `.exe` en arrière-plan et l'ajouter au démarrage de Windows.

3. *(Recommandé)* Configurez l'exécutable en mode administrateur pour garantir la capture du raccourci global :
   - Rendez-vous dans le dossier `dist/`.
   - Clic droit sur `token_box.exe` > **Propriétés** > **Compatibilité**.
   - Cochez **Exécuter ce programme en tant qu'administrateur**.

---

## 🚀 Utilisation

1. Lancez `dist/token_box.exe` (ou redémarrez votre session).
2. Appuyez sur **`CTRL + SHIFT + O`**.
3. **Ajouter un token** : Cliquez sur *Ajouter*, entrez son nom (ex: `GitHub_Personal`) et collez sa valeur.
4. **Copier un token** : Faites `CTRL + SHIFT + O`, double-cliquez sur le token souhaité, puis collez-le (`CTRL + V`) où vous en avez besoin.

---

## 🧰 Stack technique

- **GUI** : Tkinter (Python)
- **Gestion des secrets** : `keyring` (Windows Credential Manager)
- **Raccourcis & Presse-papier** : `keyboard`, `pyperclip`
- **Packaging** : PyInstaller
