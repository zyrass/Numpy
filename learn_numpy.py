import os
import sys
import subprocess

def clear_console():
    # Nettoie l'affichage de la console (Windows / Unix)
    os.system('cls' if os.name == 'nt' else 'clear')

def run_script(script_name):
    # Exécute un script Python dans un sous-processus
    print(f"\n--- EXECUTION DE : {script_name} ---")
    print("-" * 50)
    try:
        subprocess.run([sys.executable, script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Une erreur est survenue lors de l'exécution : {e}")
    except FileNotFoundError:
        print(f"\n❌ Le fichier {script_name} n'a pas été trouvé dans le répertoire courant.")
    print("-" * 50)
    print("--- FIN DE L'EXECUTION ---\n")
    input("Appuyez sur Entrée pour revenir au menu principal...")

def main():
    # Définition des modules de cours
    scripts = {
        "1": ("01_creation_tableaux.py", "Création de Tableaux (listes, zeros, ones, linspace...)"),
        "2": ("02_proprietes_tableaux.py", "Propriétés et Attributs (shape, ndim, dtype...)"),
        "3": ("03_nombres_aleatoires.py", "Génération Aléatoire (np.random.rand, seed...)"),
        "4": ("04_operations_arithmetiques.py", "Opérations et Calcul Matriciel (+, -, *, @...)"),
        "5": ("05_indexation_slicing.py", "Indexation, Slicing et Filtrage Booléen"),
        "6": ("06_fonctions_statistiques.py", "Fonctions Mathématiques et Statistiques (mean, axis...)"),
        "7": ("07_manipulation_forme.py", "Modification de la Forme (reshape, transpose, ravel)"),
        "8": ("08_donnees_manquantes.py", "Traitement des Données Manquantes (NaN, masked arrays)")
    }
    
    while True:
        clear_console()
        print("=" * 75)
        print("         🎓  FORMATION INTERACTIVE À LA BIBLIOTHÈQUE NUMPY  🎓")
        print("=" * 75)
        print("Sélectionnez le chapitre de cours que vous souhaitez étudier :\n")
        
        for key, (script, desc) in scripts.items():
            print(f"  [{key}] {desc}")
            
        print("\n  [A] Exécuter la formation complète (tous les chapitres d'un coup)")
        print("  [Q] Quitter le programme")
        print("=" * 75)
        
        choice = input("\nVotre choix : ").strip().lower()
        
        if choice in scripts:
            run_script(scripts[choice][0])
        elif choice == 'a':
            clear_console()
            print("🚀 Lancement de la formation complète NumPy...\n")
            for key, (script, desc) in scripts.items():
                print(f"\n" + "#" * 80)
                print(f"### CHAPITRE {key} : {desc.upper()}")
                print("#" * 80)
                subprocess.run([sys.executable, script])
                print("\n")
            print("=" * 80)
            print("🎉 FORMATION COMPLÈTE TERMINÉE AVEC SUCCÈS !")
            print("=" * 80)
            input("\nAppuyez sur Entrée pour revenir au menu principal...")
        elif choice == 'q':
            print("\n🐍 Merci d'avoir suivi ce cours ! Bonne programmation avec NumPy ! 👋\n")
            break
        else:
            input("Choix invalide. Appuyez sur Entrée pour réessayer...")

if __name__ == "__main__":
    main()
