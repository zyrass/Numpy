import numpy as np

def print_separator(title):
    print("\n" + "=" * 80)
    print(f" {title.upper()} ")
    print("=" * 80)

# =====================================================================
# CHAPITRE 1 : CRÉATION DE VECTEURS ET MATRICES AVEC LA CLASSE NDARRAY
# =====================================================================
print_separator("Chapitre 1 : Création de Tableaux NumPy (ndarray)")
print("NumPy propose plusieurs manières de créer des tableaux multidimensionnels.")

# --- 1.1 À partir d'une liste Python ---
print_separator("1.1 Création à partir de listes Python")

# Vecteur 1D (Tenseur d'ordre 1)
# Un tableau unidimensionnel, semblable à une liste simple mais optimisé en mémoire.
a = np.array([1, 2, 3])
print("👉 Tenseur d'ordre 1 (Vecteur 1D) :")
print(a)
print(f"Type : {type(a)}\n")

# Matrice 2D (Tenseur d'ordre 2)
# Un tableau bidimensionnel (lignes, colonnes), très utile pour représenter des images ou des tableaux de données.
b = np.array([[1, 2, 3], [4, 5, 6]])
print("👉 Tenseur d'ordre 2 (Matrice 2D) :")
print(b)
print()

# Tableau 3D (Tenseur d'ordre 3)
# Une collection de matrices (profondeur, lignes, colonnes), souvent utilisée pour des images en couleur (RGB).
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("👉 Tenseur d'ordre 3 (Tableau 3D) :")
print(c)
print()


# --- 1.2 Tableaux Pré-initialisés ---
print_separator("1.2 Tableaux pré-initialisés (zeros, ones, full, empty)")

# np.zeros
# Signature : np.zeros(shape, dtype=float, order='C')
# Label : Initialisation de zéros
# Description : Génère un tableau rempli de zéros avec la forme spécifiée (lignes, colonnes).
zeros = np.zeros((2, 3))
print("👉 Tableau de zéros (np.zeros) de forme 2x3 :")
print(zeros)
print("Note: Par défaut, le type est décimal (float64).\n")

# np.ones
# Signature : np.ones(shape, dtype=None, order='C')
# Label : Initialisation de uns
# Description : Génère un tableau rempli de uns avec la forme spécifiée.
ones = np.ones((2, 3))
print("👉 Tableau de uns (np.ones) de forme 2x3 :")
print(ones)
print()

# np.full
# Signature : np.full(shape, fill_value, dtype=None, order='C')
# Label : Initialisation avec une valeur constante
# Description : Crée un tableau avec une forme spécifiée et le remplit avec une valeur donnée (ex: 69).
full = np.full((2, 3), 69)
print("👉 Tableau rempli d'une valeur personnalisée (np.full) de forme 2x3 avec la valeur 69 :")
print(full)
print()

# np.empty
# Signature : np.empty(shape, dtype=float, order='C')
# Label : Tableau non initialisé
# Description : Crée un tableau sans initialiser ses valeurs (contient ce qui se trouvait en mémoire à ce moment-là). Plus rapide à allouer.
empty = np.empty((2, 3))
print("👉 Tableau vide non initialisé (np.empty) de forme 2x3 (valeurs aléatoires/résiduelles de la mémoire) :")
print(empty)
print()


# --- 1.3 Générateurs de Séquences ---
print_separator("1.3 Séquences numériques (linspace et arange)")

# np.linspace
# Signature : np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
# Label : Espacement linéaire (linéairement réparti)
# Description : Génère 'num' valeurs réparties de manière uniforme et égale entre 'start' et 'stop' (inclusifs).
linspace = np.linspace(-10, 20, 5)
print("👉 Tableau généré avec np.linspace (5 valeurs espacées uniformément de -10 à 20) :")
print(linspace)
print()

# np.arange
# Signature : np.arange([start, ]stop, [step, ]dtype=None, *, like=None)
# Label : Espacement par pas (séquence d'entiers ou décimaux)
# Description : Génère des valeurs espacées d'un pas 'step' donné depuis 'start' (inclus) jusqu'à 'stop' (exclus).
arange = np.arange(-5, 20, 3)
print("👉 Tableau généré avec np.arange (de -5 à 20 exclu avec un pas de 3) :")
print(arange)
print()
