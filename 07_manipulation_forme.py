import numpy as np

def print_separator(title):
    print("\n" + "=" * 80)
    print(f" {title.upper()} ")
    print("=" * 80)

# =====================================================================
# CHAPITRE 7 : MANIPULATION DE LA FORME DES TABLEAUX (RESHAPE, TRANSPOSE, RAVEL)
# =====================================================================
print_separator("Chapitre 7 : Modification de la forme des tableaux")
print("NumPy offre des moyens performants pour réorganiser la structure dimensionnelle d'un tableau sans copier les données en mémoire.")

# Tableau initial 2D (2 lignes, 3 colonnes)
a = np.array([[1, 2, 3], [4, 5, 6]])
print("\nTableau initial 'a' (2x3) :")
print(a)


# --- 7.1 Redimensionnement (.reshape) ---
print_separator("7.1 Redimensionnement (reshape)")
# Label : reshape (nouvelle forme)
# Description : Modifie la forme (shape) du tableau sans changer ses données. Le nombre total d'éléments doit rester identique (ex: 2 lignes x 3 colonnes = 6 éléments. On peut le reshape en 3x2, 6x1, 1x6, etc.).

# Reshape en 3x2
a_reshaped = a.reshape(3, 2)
print("👉 Redimensionnement en 3 lignes, 2 colonnes (a.reshape(3, 2)) :")
print(a_reshaped)
print()

# Utilisation du raccourci -1
# Label : Utilisation du paramètre -1
# Description : En passant -1 pour l'une des dimensions, NumPy calcule automatiquement sa valeur pour correspondre au nombre d'éléments restants.
auto_reshaped = a.reshape(6, -1)
print("👉 Redimensionnement avec dimension automatique (a.reshape(6, -1)) :")
print(auto_reshaped)
print(f"Forme automatique détectée par NumPy : {auto_reshaped.shape}")


# --- 7.2 Transposition (.T) ---
print_separator("7.2 Transposition (.T)")
# Label : .T (Transposition)
# Description : Intervertit les lignes et les colonnes d'une matrice. La ligne i devient la colonne i et inversement.
transposed = a.T
print("👉 Transposée de la matrice 'a' (a.T) :")
print(transposed)
print(f"Forme initiale : {a.shape}  |  Forme après transposition : {transposed.shape}")


# --- 7.3 Aplatissement (.ravel) ---
print_separator("7.3 Aplatir un tableau (ravel)")
# Label : ravel (aplatissement en 1D)
# Description : Convertit un tableau multidimensionnel en un tableau 1D (un simple vecteur). Contrairement à .flatten(), .ravel() renvoie une vue (view) plutôt qu'une copie physique de la mémoire lorsque c'est possible, ce qui le rend beaucoup plus rapide.
flattened = a.ravel()
print("👉 Tableau aplati en 1D (a.ravel()) :")
print(flattened)
print(f"Forme finale : {flattened.shape}")
