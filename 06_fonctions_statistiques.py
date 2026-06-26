import numpy as np

def print_separator(title):
    print("\n" + "=" * 80)
    print(f" {title.upper()} ")
    print("=" * 80)

# =====================================================================
# CHAPITRE 6 : FONCTIONS MATHÉMATIQUES ET STATISTIQUES
# =====================================================================
print_separator("Chapitre 6 : Fonctions Mathématiques et Statistiques")
print("NumPy offre des fonctions hautement optimisées pour effectuer des calculs statistiques sur les tableaux.")

# Tableaux de test
a = np.array([1, 2, 3, 4, 5])
matrice = np.array([[1, 2], [3, 4]])

print("\nDonnées de test :")
print("a (1D) :", a)
print("matrice (2D) :")
print(matrice)


# --- 6.1 Statistiques Globales ---
print_separator("6.1 Calculs statistiques globaux")

# Somme globale
print(f"👉 Somme globale de 'a' (np.sum) : {np.sum(a)}")

# Produit global
print(f"👉 Produit global de 'a' (np.prod) : {np.prod(a)}")

# Moyenne globale
print(f"👉 Moyenne arithmétique de 'a' (np.mean) : {np.mean(a)}")

# Médiane globale
print(f"👉 Valeur médiane de 'a' (np.median) : {np.median(a)}")

# Écart-type (Standard Deviation)
print(f"👉 Écart-type de 'a' (np.std) : {np.std(a):.4f} (mesure de la dispersion autour de la moyenne)")


# --- 6.2 Calculs par Axes (Clé pour débutants) ---
print_separator("6.2 Calculs sur les lignes ou colonnes (Notion d'Axe)")
print("Pour les tableaux à 2 dimensions (matrices) :")
print("  - axis=0 : Calcul le long des colonnes (verticalement)")
print("  - axis=1 : Calcul le long des lignes (horizontalement)\n")

# Somme par colonnes (axis=0)
somme_col = np.sum(matrice, axis=0)
print("👉 Somme le long de l'axe 0 (par colonne) [1+3, 2+4] :")
print(somme_col)
print()

# Somme par lignes (axis=1)
somme_lig = np.sum(matrice, axis=1)
print("👉 Somme le long de l'axe 1 (par ligne) [1+2, 3+4] :")
print(somme_lig)
print()

# Moyenne par colonne
mean_col = np.mean(matrice, axis=0)
print("👉 Moyennes par colonne (axis=0) :")
print(mean_col)


# --- 6.3 Fonctions Universelles (ufuncs) ---
print_separator("6.3 Fonctions mathématiques universelles (ufuncs)")
print("Ces fonctions s'appliquent à chaque élément de manière individuelle.")

# Racine carrée (np.sqrt)
print("👉 Racine carrée de chaque élément de 'a' (np.sqrt) :")
print(np.sqrt(a))
print()

# Exponentielle (np.exp)
print("👉 Exponentielle (e^x) de chaque élément de 'a' (np.exp) :")
print(np.exp(a))
