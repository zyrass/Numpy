import numpy as np

def print_separator(title):
    print("\n" + "=" * 80)
    print(f" {title.upper()} ")
    print("=" * 80)

# =====================================================================
# CHAPITRE 2 : PROPRIÉTÉS ET ATTRIBUTS DES TABLEAUX NUMPY
# =====================================================================
print_separator("Chapitre 2 : Propriétés et Attributs des Tableaux")
print("Chaque tableau NumPy (ndarray) possède des attributs clés qui décrivent sa structure physique et logique.")

# Définissons deux tableaux de test
vecteur = np.array([10, 20, 30, 40])
matrice = np.full((3, 4), 7.5) # Tableau 2D de dimension 3x4 rempli de 7.5

print("\nTableaux utilisés pour les exemples :")
print("1) vecteur :")
print(vecteur)
print("2) matrice :")
print(matrice)

# --- 2.1 Nombre de dimensions (.ndim) ---
print_separator("2.1 Le nombre de dimensions (.ndim)")
# Label : ndim (nombre d'axes ou dimensions)
# Description : Renvoie le nombre de dimensions (d'axes) du tableau sous forme d'un entier.
print(f"👉 Nombre de dimensions du 'vecteur' (ndim) : {vecteur.ndim}  (car c'est un vecteur 1D)")
print(f"👉 Nombre de dimensions de la 'matrice' (ndim) : {matrice.ndim}  (car c'est une matrice 2D à lignes et colonnes)")

# --- 2.2 Forme du tableau (.shape) ---
print_separator("2.2 La forme du tableau (.shape)")
# Label : shape (dimensions sous forme de tuple)
# Description : Renvoie la taille du tableau le long de chaque axe sous forme de tuple d'entiers.
print(f"👉 Forme du 'vecteur' (shape) : {vecteur.shape}  (contient 4 éléments sur sa seule dimension)")
print(f"👉 Forme de la 'matrice' (shape) : {matrice.shape}  (indique 3 lignes et 4 colonnes)")

# --- 2.3 Nombre total d'éléments (.size) ---
print_separator("2.3 Le nombre total d'éléments (.size)")
# Label : size (nombre total d'éléments)
# Description : Renvoie le nombre total d'éléments présents dans le tableau. C'est le produit des dimensions renvoyées par shape.
print(f"👉 Nombre total d'éléments dans le 'vecteur' (size) : {vecteur.size}")
print(f"👉 Nombre total d'éléments dans la 'matrice' (size) : {matrice.size}  (soit 3 lignes * 4 colonnes = 12)")

# --- 2.4 Type de données (.dtype) ---
print_separator("2.4 Le type de données (.dtype)")
# Label : dtype (type des éléments)
# Description : Indique le type de données stockées dans le tableau. Contrairement aux listes Python ordinaires, tous les éléments d'un tableau NumPy doivent être du même type.
print(f"👉 Type des données du 'vecteur' (dtype) : {vecteur.dtype}  (entiers 32/64 bits)")
print(f"👉 Type des données de la 'matrice' (dtype) : {matrice.dtype}  (nombres décimaux float64)")

# --- 2.5 Taille de chaque élément (.itemsize) ---
print_separator("2.5 La taille en octets de chaque élément (.itemsize)")
# Label : itemsize (taille en octets de chaque élément)
# Description : Renvoie la taille en octets (bytes) occupée par chaque élément individuel du tableau.
print(f"👉 Taille de chaque élément de 'vecteur' (itemsize) : {vecteur.itemsize} octets")
print(f"👉 Taille de chaque élément de 'matrice' (itemsize) : {matrice.itemsize} octets")
print(f"👉 Espace total occupé par la matrice en mémoire (size * itemsize) : {matrice.size * matrice.itemsize} octets")
