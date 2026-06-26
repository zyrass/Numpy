import numpy as np

def print_separator(title):
    print("\n" + "=" * 80)
    print(f" {title.upper()} ")
    print("=" * 80)

# =====================================================================
# CHAPITRE 5 : INDEXATION, SLICING ET FILTRAGE BOOLÉEN
# =====================================================================
print_separator("Chapitre 5 : Indexation et Slicing (Sélection de données)")
print("L'indexation permet de lire et modifier des éléments individuels ou des portions de tableaux (slicing).")

# Tableaux de test
a = np.array([10, 20, 30, 40, 50])
matrice = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("\nTableaux de test :")
print("a (1D) :", a)
print("matrice (2D) :")
print(matrice)


# --- 5.1 Indexation Unidimensionnelle (1D) ---
print_separator("5.1 Indexation et Slicing en 1D")

# Accès simple
print(f"👉 Accès au premier élément (indice 0) : {a[0]}")
print(f"👉 Accès au troisième élément (indice 2) : {a[2]}")
print(f"👉 Accès au dernier élément (indice négatif -1) : {a[-1]}\n")

# Slicing
# Syntaxe : a[début:fin:pas] (fin est exclusif)
print(f"👉 Slicing de l'indice 1 à 3 (exclu) : {a[1:3]}")
print(f"👉 Les 3 premiers éléments : {a[:3]}")
print(f"👉 Éléments avec un pas de 2 : {a[::2]}")
print(f"👉 Inverser le tableau : {a[::-1]}")


# --- 5.2 Indexation Bidimensionnelle (2D) ---
print_separator("5.2 Indexation et Slicing en 2D (Matrices)")
print("Syntaxe : matrice[indice_ligne, indice_colonne]")

# Accès simple
print(f"👉 Élément ligne 0, colonne 1 : {matrice[0, 1]} (valeur attendue: 2)")
print(f"👉 Élément ligne 2, colonne 2 : {matrice[2, 2]} (valeur attendue: 9)\n")

# Slicing en 2D
print("👉 Récupérer la deuxième ligne complète (ligne indice 1) :")
print(matrice[1, :])
print()

print("👉 Récupérer la première colonne complète (colonne indice 0) :")
print(matrice[:, 0])
print()

print("👉 Sous-matrice (2 premières lignes, 2 dernières colonnes) :")
print(matrice[0:2, 1:3])


# --- 5.3 Filtrage Booléen (Indexation Booléenne) ---
print_separator("5.3 Filtrage conditionnel (Indexation Booléenne)")
print("NumPy permet de filtrer des tableaux en utilisant des expressions conditionnelles. C'est magique !")

# Créer un masque de vérité (True/False)
masque = (a > 25)
print("👉 Etape 1: Création du masque conditionnel (a > 25) :")
print(masque)
print()

# Appliquer le masque pour extraire les valeurs
valeurs_filtrees = a[masque]
print("👉 Etape 2: Extraction des valeurs valant True dans le masque :")
print(valeurs_filtrees)
print()

# Version condensée
print("👉 Version directe en une ligne (a[a > 20]) :")
print(a[a > 20])
print()

# Remplacement avec masque
copie_a = a.copy()
copie_a[copie_a < 30] = 999
print("👉 Remplacement des éléments < 30 par la valeur 999 :")
print(copie_a)
