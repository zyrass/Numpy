import numpy as np

###########################################################################################################################
# 1 - CREATION DE VECTEURS ET MATRICES AVEC LA CLASS NDARRAY
###########################################################################################################################

# Création d'un tableau à partir d'une liste
a = np.array([1, 2, 3])  # Crée un array avec des valeurs personnalisées
b = np.array([[1, 2, 3], [4, 5, 6]])  # Crée un array 2D
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Crée un array 3D

print(f"Tenseur d'ordre 1:\n{a}\n")
print(f"Tenseur d'ordre 2:\n{b}\n")
print(f"Tenseur d'ordre 3:\n{c}\n")

# Création d'un tableau de zéros
# Signature : np.zeros(shape, dtype=float, order='C')
# Description : Génère un array rempli de zéros avec une forme spécifiée par `shape`.
zeros = np.zeros((2, 3))
print(f"Tableau de zéros (2x3):\n{zeros}\n")

# Création d'un tableau de uns
# Signature : np.ones(shape, dtype=None, order='C')
# Description : Génère un array rempli de uns avec une forme spécifiée par `shape`.
ones = np.ones((2, 3))
print(f"Tableau de uns (2x3):\n{ones}\n")

# Création d'un tableau avec une valeur personnalisée
# Signature : np.full(shape, fill_value, dtype=None, order='C')
# Description : Crée un array avec une forme spécifiée par `shape` et le remplit avec `fill_value`.
full = np.full((5, 6), 69)
print(f"Tableau de valeur 69 (5x6):\n{full}\n")

# Création d'un tableau avec un intervalle défini entre un début et une fin
# Signature : np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
# Description : Génère des valeurs espacées uniformément entre `start` et `stop`.
linspace = np.linspace(-10, 20, 5)
print(f"Tableau linspace de -10 à 20 avec 5 valeurs:\n{linspace}\n")

# Création d'un tableau avec un pas (step) entre un début et une fin
# Signature : np.arange([start, ]stop, [step, ]dtype=None, *, like=None)
# Description : Génère des valeurs espacées régulièrement entre `start` et `stop` avec un pas `step`.
arange = np.arange(-5, 20, 3)
print(f"Tableau arange de -5 à 20 avec un pas de 3:\n{arange}\n")

###########################################################################################################################
# 2 - ATTRIBUTS à connaître
###########################################################################################################################

# Renvoie les dimensions d'un array sous forme d'un tuple
print(f"Dimensions de 'full': {full.shape}")

# Renvoie le nombre d'éléments d'un array sous forme d'un entier
print(f"Nombre d'éléments dans 'full': {full.size}")

# Renvoie le nombre de dimensions d'un array sous forme d'un entier
print(f"Nombre de dimensions de 'full': {full.ndim}")

print(f"Dimensions de 'c': {c.shape}")
print(f"Nombre de dimensions de 'c': {c.ndim}")

###########################################################################################################################
# 3 - SOUS-MODULE RANDOM
###########################################################################################################################

# Génère un tableau 1D de nombres aléatoires uniformes entre 0 et 1
# Signature : np.random.rand(d0, d1, ..., dn)
# Description : Renvoie un ou plusieurs échantillons, tirés uniformément entre [0, 1) de la distribution continue uniforme.
rand_1 = np.random.rand(5)
print(f"Tableau de nombres aléatoires uniformes (1D, 5 éléments):\n{rand_1}\n")

# Génère un tableau 2D de nombres aléatoires uniformes entre 0 et 1
rand_2 = np.random.rand(4, 2)
print(f"Tableau de nombres aléatoires uniformes (2D, 4x2):\n{rand_2}\n")

# Génère un tableau 1D de nombres aléatoires selon une distribution normale (moyenne=0, écart-type=1)
# Signature : np.random.randn(d0, d1, ..., dn)
# Description : Renvoie un ou plusieurs échantillons, tirés de la distribution normale standard (moyenne=0, écart-type=1).
randn_1 = np.random.randn(25)
print(f"Tableau de nombres aléatoires normaux (1D, 25 éléments):\n{randn_1}\n")

# Génère un tableau 2D de nombres aléatoires selon une distribution normale
randn_2 = np.random.randn(4, 2)
print(f"Tableau de nombres aléatoires normaux (2D, 4x2):\n{randn_2}\n")

# Génère un tableau 1D de nombres entiers aléatoires dans une plage spécifiée
# Signature : np.random.randint(low, high=None, size=None, dtype='l')
# Description : Renvoie des entiers aléatoires de `low` (inclusif) à `high` (exclusif).
randint_1 = np.random.randint(10, size=5)
print(f"Tableau de nombres entiers aléatoires (1D, 5 éléments, de 0 à 9):\n{randint_1}\n")

# Génère un tableau 1D de nombres entiers aléatoires dans une plage spécifiée
randint_2 = np.random.randint(0, 255, size=5)
print(f"Tableau de nombres entiers aléatoires (1D, 5 éléments, de 0 à 254):\n{randint_2}\n")

# Génère un tableau 1D de nombres entiers aléatoires dans une plage spécifiée
randint_3 = np.random.randint(-255, 255, size=20)
print(f"Tableau de nombres entiers aléatoires (1D, 20 éléments, de -255 à 254):\n{randint_3}\n")

###########################################################################################################################
# 4 - CALCUL MATRICIEL
###########################################################################################################################

# ---- ADDITION
# Signature : np.add(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None)
# Description : Additionne les éléments correspondants de deux arrays de même forme.
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
addition = np.add(a, b)
print(f"Addition de a et b:\n{addition}\n")

# ---- SOUSTRATION
# Signature : np.subtract(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None)
# Description : Soustrait les éléments correspondants de deux arrays de même forme.
soustraction = np.subtract(a, b)
print(f"Soustraction de b à a:\n{soustraction}\n")

# ---- MULTIPLICATION d'un scalaire
# Signature : np.multiply(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None)
# Description : Multiplie chaque élément d'un array par un scalaire.
scalaire = 2
multiplication_scalaire = np.multiply(a, scalaire)
print(f"Multiplication de a par {scalaire}:\n{multiplication_scalaire}\n")

# ---- PRODUIT TERME A TERME de même dimensions
# Signature : np.multiply(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None)
# Description : Multiplie les éléments correspondants de deux arrays de même forme terme à terme.
produit_terme_terme = np.multiply(a, b)
print(f"Produit terme à terme de a et b:\n{produit_terme_terme}\n")

# ---- PRODUIT MATRICIEL
# Signature : np.dot(a, b, out=None)
# Description : Effectue le produit matriciel de deux arrays. Pour 2D arrays, cela correspond à une multiplication matricielle standard.
produit_matriciel = np.dot(a, b)
print(f"Produit matriciel de a et b:\n{produit_matriciel}\n")

###########################################################################################################################
# 5 - INDEXING - SLICING - BOOLEANN INDEXING
###########################################################################################################################

