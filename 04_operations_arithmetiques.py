import numpy as np

def print_separator(title):
    print("\n" + "=" * 80)
    print(f" {title.upper()} ")
    print("=" * 80)

# =====================================================================
# CHAPITRE 4 : OPÉRATIONS ARITHMÉTIQUES ET CALCUL MATRICIEL
# =====================================================================
print_separator("Chapitre 4 : Calculs et Opérations sur Tableaux")
print("NumPy permet d'effectuer des opérations ultra-rapides sans boucle 'for' grâce à la vectorisation.")

# Tableaux de test
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("\nMatrices de test (2x2) :")
print("a =")
print(a)
print("b =")
print(b)


# --- 4.1 Opérations Elémentaires ---
print_separator("4.1 Opérations arithmétiques terme à terme")
print("Ces opérations sont appliquées élément par élément. On peut utiliser les fonctions de NumPy ou les opérateurs standard (+, -, *, /).")

# ADDITION
# Signature : np.add(x1, x2, ...)
# Label : Addition matricielle terme à terme
# Description : Additionne les éléments aux positions correspondantes.
addition_func = np.add(a, b)
addition_op = a + b
print("👉 Addition (a + b) :")
print(addition_op)
print("Note: np.add(a, b) et a + b donnent le même résultat.\n")

# SOUSTRACTION
# Signature : np.subtract(x1, x2, ...)
# Label : Soustraction matricielle terme à terme
# Description : Soustrait les éléments de b à ceux de a.
soustraction_func = np.subtract(a, b)
soustraction_op = a - b
print("👉 Soustraction (a - b) :")
print(soustraction_op)
print()

# DIVISION
# Signature : np.divide(x1, x2, ...)
# Label : Division matricielle terme à terme
# Description : Divise chaque élément du premier tableau par celui correspondant du second.
division_func = np.divide(a, b)
division_op = a / b
print("👉 Division (a / b) :")
print(division_op)
print()


# --- 4.2 Multiplications (Scalaire vs Terme à Terme vs Matricielle) ---
print_separator("4.2 Les différents types de multiplications")

# MULTIPLICATION PAR UN SCALAIRE
# Signature : np.multiply(x1, scalar)
# Label : Multiplication par un scalaire
# Description : Multiplie chaque élément du tableau par un seul nombre.
scalaire = 2
multiplication_scalaire = a * scalaire
print(f"👉 Multiplication par un scalaire (a * {scalaire}) :")
print(multiplication_scalaire)
print()

# PRODUIT TERME À TERME (Element-wise)
# Signature : np.multiply(x1, x2)
# Label : Produit terme à terme (Hadamard)
# Description : Multiplie chaque élément d'un tableau par l'élément correspondant à la même position. Les dimensions doivent correspondre.
produit_terme_terme = np.multiply(a, b)
print("👉 Produit terme à terme (a * b ou np.multiply) :")
print(produit_terme_terme)
print("Attention : Ce n'est PAS la multiplication de matrices de l'algèbre linéaire.\n")

# PRODUIT MATRICIEL (Algèbre Linéaire)
# Signature : np.dot(a, b) ou a @ b
# Label : Produit matriciel
# Description : Calcule le produit matriciel classique de l'algèbre linéaire (combinaison linéaire des lignes par colonnes).
produit_matriciel_dot = np.dot(a, b)
produit_matriciel_op = a @ b
print("👉 Produit matriciel (a @ b ou np.dot(a, b)) :")
print(produit_matriciel_op)
print("Note: L'opérateur '@' est la notation recommandée en Python 3 pour le produit matriciel.")
