import numpy as np

def print_separator(title):
    print("\n" + "=" * 80)
    print(f" {title.upper()} ")
    print("=" * 80)

# =====================================================================
# CHAPITRE 8 : GESTION DES VALEURS MANQUANTES (NaN) ET TABLEAUX MASQUÉS
# =====================================================================
print_separator("Chapitre 8 : Traitement des Données Manquantes")
print("Dans le traitement réel de données, il est fréquent d'avoir des valeurs manquantes ou corrompues. NumPy dispose d'outils performants pour les gérer.")

# Création d'un tableau contenant une valeur manquante (np.nan)
# Note: np.nan est un nombre décimal spécial (float), donc le tableau doit être de type float.
a = np.array([1.0, 2.0, np.nan, 4.0])
print("\nTableau initial contenant une valeur manquante (np.nan) :")
print("a =", a)


# --- 8.1 Le piège de la comparaison avec NaN ---
print_separator("8.1 Le piège de np.nan (Pourquoi a == np.nan ne fonctionne pas)")
# Warning/Important info: np.nan n'est jamais égal à lui-même. Par conséquent, 'a == np.nan' renverra toujours False pour tous les éléments !
print("❌ Mauvaise méthode (a == np.nan) :")
print(a == np.nan)
print("Remarquez que le troisième élément est évalué à False alors qu'il s'agit bien d'un NaN !")

print("\n✅ Bonne méthode (np.isnan(a)) :")
print(np.isnan(a))
print("C'est la fonction np.isnan() qui permet de détecter correctement les valeurs manquantes.\n")


# --- 8.2 Masquer les données (np.ma.masked_array) ---
print_separator("8.2 Les tableaux masqués (np.ma.masked_array)")
# Label : np.ma.masked_array (Masquage de données)
# Description : Permet de créer un tableau où certaines valeurs sont ignorées (masquées) lors des calculs statistiques (somme, moyenne, etc.) sans pour autant modifier le tableau d'origine.

# Créer un tableau masqué où les NaNs sont masqués
masque_nan = np.isnan(a)
masked_array = np.ma.masked_array(a, mask=masque_nan)

print("👉 Tableau masqué (masked_array) :")
print(masked_array)
print()

# Calculer la moyenne globale
# Si on fait la moyenne du tableau d'origine 'a', le résultat sera 'nan' car nan + n'importe quoi = nan.
print(f"👉 Moyenne du tableau original 'a' (np.mean(a)) : {np.mean(a)}")
# Avec le tableau masqué, NumPy ignore les valeurs masquées lors des calculs.
print(f"👉 Moyenne du tableau masqué (np.mean(masked_array)) : {np.mean(masked_array)}  (calcule (1+2+4)/3 = 2.33)")


# --- 8.3 Remplacer les données manquantes ---
print_separator("8.3 Remplacer les valeurs manquantes (imputation)")
# Label : Remplacement de NaN
# Description : Permet de remplacer toutes les valeurs manquantes détectées par np.isnan par une valeur par défaut (ex: 0 ou la moyenne).

copie_a = a.copy()
# On sélectionne les indices où np.isnan(copie_a) vaut True, et on leur affecte 0.0
copie_a[np.isnan(copie_a)] = 0.0

print("👉 Tableau après remplacement des NaN par 0.0 :")
print(copie_a)
print()

# Autre exemple : remplacer par la moyenne des valeurs valides
copie_moyenne = a.copy()
moyenne_valides = np.nanmean(a) # np.nanmean calcule la moyenne en ignorant les NaN d'office
copie_moyenne[np.isnan(copie_moyenne)] = moyenne_valides

print(f"👉 Tableau après remplacement des NaN par la moyenne des éléments valides ({moyenne_valides}) :")
print(copie_moyenne)
