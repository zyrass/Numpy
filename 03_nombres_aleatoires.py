import numpy as np

def print_separator(title):
    print("\n" + "=" * 80)
    print(f" {title.upper()} ")
    print("=" * 80)

# =====================================================================
# CHAPITRE 3 : GÉNÉRATION DE NOMBRES ALÉATOIRES AVEC LE SOUS-MODULE RANDOM
# =====================================================================
print_separator("Chapitre 3 : Le Sous-module Aléatoire (np.random)")
print("Le sous-module random permet de générer des tableaux de nombres aléatoires selon diverses distributions de probabilité.")

# Fixer la graine aléatoire (seed)
# Label : np.random.seed (Reproductibilité)
# Description : Permet de bloquer le générateur pseudo-aléatoire sur une séquence fixe afin d'obtenir toujours les mêmes résultats à chaque exécution. C'est essentiel pour reproduire des expériences scientifiques ou de machine learning.
np.random.seed(42)
print("ℹ️ Note: La graine aléatoire (seed) est fixée à 42 pour garantir des résultats identiques à chaque exécution.\n")


# --- 3.1 Distribution Uniforme (.rand) ---
print_separator("3.1 Distribution Uniforme entre 0 et 1 (np.random.rand)")
# Signature : np.random.rand(d0, d1, ..., dn)
# Label : Aléatoire Uniforme
# Description : Génère un tableau de formes données rempli de valeurs tirées uniformément dans l'intervalle semi-ouvert [0.0, 1.0[.

rand_1d = np.random.rand(5)
print("👉 Tableau 1D de 5 nombres aléatoires uniformes [0, 1) :")
print(rand_1d)
print()

rand_2d = np.random.rand(4, 2)
print("👉 Tableau 2D (forme 4x2) de nombres aléatoires uniformes :")
print(rand_2d)
print()


# --- 3.2 Distribution Normale Standard (.randn) ---
print_separator("3.2 Distribution Normale Standard (np.random.randn)")
# Signature : np.random.randn(d0, d1, ..., dn)
# Label : Aléatoire selon une loi Normale
# Description : Génère un tableau de formes données rempli de valeurs tirées selon la distribution normale standard (courbe en cloche, de moyenne 0 et d'écart-type 1). Les valeurs sont souvent comprises entre -3 et 3.

randn_1d = np.random.randn(5)
print("👉 Tableau 1D de 5 nombres aléatoires normaux (moyenne=0, écart-type=1) :")
print(randn_1d)
print()

randn_2d = np.random.randn(4, 2)
print("👉 Tableau 2D (forme 4x2) de nombres aléatoires normaux :")
print(randn_2d)
print()


# --- 3.3 Entiers Aléatoires (.randint) ---
print_separator("3.3 Entiers Aléatoires dans une Plage (np.random.randint)")
# Signature : np.random.randint(low, high=None, size=None, dtype='l')
# Label : Entiers Aléatoires
# Description : Renvoie des entiers aléatoires de 'low' (inclus) à 'high' (exclus). Si 'high' n'est pas spécifié, la plage est de 0 à 'low'.

randint_1 = np.random.randint(10, size=5)
print("👉 Tableau 1D de 5 entiers compris de 0 à 9 (high non spécifié) :")
print(randint_1)
print()

randint_2 = np.random.randint(0, 255, size=5)
print("👉 Tableau 1D de 5 entiers compris de 0 à 254 (idéal pour représenter des pixels RGB) :")
print(randint_2)
print()

randint_3 = np.random.randint(-255, 255, size=10)
print("👉 Tableau 1D de 10 entiers compris de -255 à 254 :")
print(randint_3)
print()
