# 🎓 Guide Complet NumPy : De Débutant à Pro 🐍

[![NumPy](https://img.shields.io/badge/Library-NumPy-013243?style=flat-square&logo=numpy&logoColor=white)](https://numpy.org/)
[![Python](https://img.shields.io/badge/Language-Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Educational-brightgreen?style=flat-square)](#)

Bienvenue dans ce guide d'apprentissage pratique de **NumPy (Numerical Python)**, la bibliothèque fondamentale pour le calcul scientifique, l'analyse de données et le machine learning en Python.

Ce dépôt a été conçu pour qu'un **débutant complet** comprenne exactement chaque concept, pourquoi il est utilisé et comment l'implémenter.

<br>

---

<br>

#### 📌 Sommaire

1. [Pourquoi apprendre NumPy ?](#1-pourquoi-apprendre-numpy-)
2. [Installation Professionnelle](#2-installation-professionnelle-)
3. [Structure de la Formation Interactive](#3-structure-de-la-formation-interactive-)
4. [Chapitres de Cours](#4-chapitres-de-cours)
   - [Chapitre 1 : Création de Tableaux](#chapitre-1--création-de-tableaux)
   - [Chapitre 2 : Propriétés des Tableaux](#chapitre-2--propriétés-des-tableaux)
   - [Chapitre 3 : Génération Aléatoire](#chapitre-3--génération-aléatoire)
   - [Chapitre 4 : Calculs et Opérations](#chapitre-4--calculs-et-opérations)
   - [Chapitre 5 : Indexation et Slicing](#chapitre-5--indexation-et-slicing)
   - [Chapitre 6 : Fonctions Statistiques](#chapitre-6--fonctions-statistiques)
   - [Chapitre 7 : Modification de Forme](#chapitre-7--modification-de-forme)
   - [Chapitre 8 : Données Manquantes (NaN)](#chapitre-8--données-manquantes-nan)
5. [Ressources Supplémentaires](#5-ressources-supplémentaires)

<br>

---

<br>

### 1. Pourquoi apprendre NumPy ? 💡

Les listes Python standards sont flexibles mais lentes car elles peuvent contenir n'importe quel type d'objet, nécessitant des vérifications de type constantes en mémoire.

NumPy introduit le concept de **`ndarray`** (N-dimensional array) :
- **Homogénéité :** Tous les éléments possèdent le même type de données (ex: tous entiers ou tous décimaux).
- **Contiguïté en Mémoire :** Les données sont stockées de façon contiguë dans la mémoire vive. Le processeur peut donc y accéder instantanément.
- **Vectorisation :** Plus besoin de boucles `for` lentes. Les opérations mathématiques s'appliquent sur des millions de données en une seule opération CPU (écrite en C).

<br>

---

<br>

### 2. Installation Professionnelle ⚙️

Pour travailler proprement, il est fortement recommandé de créer un environnement virtuel Python (`venv`) avant d'installer NumPy.

#### Étape 1 : Créer et activer l'environnement virtuel
Dans votre terminal :

```bash
# Sur Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Sur macOS ou Linux
python3 -m venv venv
source venv/bin/activate
```

#### Étape 2 : Installer NumPy
Mettez à jour le gestionnaire de paquets `pip` puis installez la bibliothèque :

```bash
pip install --upgrade pip
pip install numpy
```

#### Étape 3 : Vérifier l'installation
Lancez Python et exécutez la commande suivante pour afficher la version installée :

```python
import numpy as np
print(np.__version__)
```

<br>

---

<br>

### 3. Structure de la Formation Interactive 📂

Pour rendre l'apprentissage progressif et structuré, le code initial a été divisé en **8 modules indépendants**. Vous pouvez les exécuter un par un ou utiliser le menu interactif principal :

| Fichier | Titre | Description |
| :--- | :--- | :--- |
| 🚀 **[learn_numpy.py](file:///j:/www/python/Numpy/learn_numpy.py)** | **Menu Principal** | **Script interactif pour lancer tous les chapitres.** |
| 📁 **[01_creation_tableaux.py](file:///j:/www/python/Numpy/01_creation_tableaux.py)** | Chapitre 1 | Création à partir de listes, zéros, uns, séquences... |
| 📁 **[02_proprietes_tableaux.py](file:///j:/www/python/Numpy/02_proprietes_tableaux.py)** | Chapitre 2 | Attributs essentiels (`shape`, `ndim`, `size`, `dtype`...). |
| 📁 **[03_nombres_aleatoires.py](file:///j:/www/python/Numpy/03_nombres_aleatoires.py)** | Chapitre 3 | Sous-module `np.random` (uniforme, normale, graine seed). |
| 📁 **[04_operations_arithmetiques.py](file:///j:/www/python/Numpy/04_operations_arithmetiques.py)** | Chapitre 4 | Opérations arithmétiques vectorisées, produit matriciel `@`. |
| 📁 **[05_indexation_slicing.py](file:///j:/www/python/Numpy/05_indexation_slicing.py)** | Chapitre 5 | Accès aux éléments 1D/2D, découpe de tableau, masques. |
| 📁 **[06_fonctions_statistiques.py](file:///j:/www/python/Numpy/06_fonctions_statistiques.py)** | Chapitre 6 | Fonctions d'agrégation, calculs statistiques, notion d'Axe. |
| 📁 **[07_manipulation_forme.py](file:///j:/www/python/Numpy/07_manipulation_forme.py)** | Chapitre 7 | Modification de dimensions, transposition et aplatissement. |
| 📁 **[08_donnees_manquantes.py](file:///j:/www/python/Numpy/08_donnees_manquantes.py)** | Chapitre 8 | Gestion des valeurs `NaN` et des tableaux masqués (`np.ma`). |

<br>

---

<br>

### 4. Chapitres de Cours

#### Chapitre 1 : Création de Tableaux

Apprenez à générer des structures de données de base.

* **🏷️ Label : `np.array`** (Création personnalisée)  
  *Permet de transformer une liste Python standard en tableau NumPy.*
  ```python
  a = np.array([1, 2, 3])
  ```
* **🏷️ Label : `np.zeros`** (Initialisation à zéro)  
  *Génère un tableau rempli uniquement de zéros (utile pour pré-allouer la mémoire).*
  ```python
  zeros = np.zeros((2, 3))
  ```
* **🏷️ Label : `np.ones`** (Initialisation à un)  
  *Génère un tableau rempli de uns.*
  ```python
  ones = np.ones((2, 3))
  ```
* **🏷️ Label : `np.linspace`** (Espacement linéaire)  
  *Génère un nombre fixe de valeurs équitablement espacées entre un début et une fin.*
  ```python
  linspace = np.linspace(-10, 20, 5) # [-10.,  -2.5,   5.,  12.5,  20.]
  ```
* **🏷️ Label : `np.arange`** (Espacement par pas)  
  *Génère une séquence de nombres avec un intervalle (pas) régulier.*
  ```python
  arange = np.arange(-5, 20, 3) # [-5, -2, 1, 4, 7, 10, 13, 16, 19]
  ```

<br>

---

<br>

#### Chapitre 2 : Propriétés des Tableaux

Découvrez comment interroger la structure d'un tableau NumPy.

* **🏷️ Label : `.ndim`** (Nombre de dimensions)  
  *Renvoie le nombre d'axes d'un tableau (1 pour un vecteur, 2 pour une matrice).*
  ```python
  print(a.ndim)
  ```
* **🏷️ Label : `.shape`** (Forme du tableau)  
  *Renvoie un tuple représentant la taille sur chaque axe (Exemple: `(lignes, colonnes)`).*
  ```python
  print(a.shape)
  ```
* **🏷️ Label : `.dtype`** (Type des données)  
  *Indique le type de données stockées (tous les éléments doivent avoir le même type).*
  ```python
  print(a.dtype) # ex: int64, float64
  ```

<br>

---

<br>

#### Chapitre 3 : Génération Aléatoire

Générez des données aléatoires pour simuler des variables statistiques.

* **🏷️ Label : `np.random.seed`** (Reproductibilité)  
  *Verrouille le générateur d'aléatoire pour que le script produise exactement les mêmes nombres à chaque exécution.*
  ```python
  np.random.seed(42)
  ```
* **🏷️ Label : `np.random.rand`** (Distribution uniforme)  
  *Tire des nombres aléatoires entre 0 et 1 de manière équitable.*
  ```python
  rand_data = np.random.rand(5)
  ```
* **🏷️ Label : `np.random.randn`** (Distribution normale)  
  *Génère des nombres selon une courbe en cloche de Gauss (moyenne = 0, écart-type = 1).*
  ```python
  randn_data = np.random.randn(5)
  ```
* **🏷️ Label : `np.random.randint`** (Entiers aléatoires)  
  *Tire des entiers aléatoires dans un intervalle spécifié.*
  ```python
  randint_data = np.random.randint(0, 10, size=5)
  ```

<br>

---

<br>

#### Chapitre 4 : Calculs et Opérations

Effectuez des calculs arithmétiques simples ou complexes sur des matrices.

* **🏷️ Label : Opérations Terme à Terme (`+`, `-`, `*`, `/`)**  
  *Les opérateurs de base appliquent les calculs élément par élément.*
  ```python
  c = a + b # Additionne chaque case correspondante
  ```
* **🏷️ Label : `np.multiply` vs `np.dot`**  
  *`np.multiply` (ou `a * b`) effectue un produit élément par élément. `np.dot` (ou `a @ b`) effectue le produit matriciel de l'algèbre linéaire (lignes x colonnes).*
  ```python
  produit_matriciel = a @ b
  ```

<br>

---

<br>

#### Chapitre 5 : Indexation et Slicing

Sélectionnez et filtrez vos données avec précision.

* **🏷️ Label : Slicing 1D et 2D (`a[start:stop:step]`)**  
  *Permet de découper une portion de votre tableau.*
  ```python
  sous_tableau = a[1:4] # Extrait les éléments aux indices 1, 2 et 3
  ```
* **🏷️ Label : Indexation Booléenne (Masques)**  
  *Permet d'extraire les éléments répondant à une condition logique.*
  ```python
  filtre = a[a > 2] # Garde uniquement les valeurs supérieures à 2
  ```

<br>

---

<br>

#### Chapitre 6 : Fonctions Statistiques

Calculez des agrégats (somme, moyenne, etc.) globalement ou par dimension.

* **🏷️ Label : `np.sum`, `np.mean`, `np.std`** (Statistiques)  
  *Calcule respectivement la somme, la moyenne et l'écart-type.*
  ```python
  print(np.mean(a))
  ```
* **🏷️ Label : Concept d'Axe (`axis`)**  
  *Dans un tableau 2D, `axis=0` effectue le calcul sur chaque colonne (de haut en bas), tandis que `axis=1` effectue le calcul sur chaque ligne (de gauche à droite).*
  ```python
  somme_par_colonne = np.sum(matrice, axis=0)
  ```

<br>

---

<br>

#### Chapitre 7 : Modification de Forme

Réorganisez les dimensions de vos tableaux de données.

* **🏷️ Label : `np.reshape`** (Changement de forme)  
  *Redéfinit la forme du tableau sans toucher aux valeurs en mémoire.*
  ```python
  matrice_3x2 = matrice_2x3.reshape(3, 2)
  ```
* **🏷️ Label : `.T`** (Transposition)  
  *Intervertit les lignes et les colonnes d'une matrice.*
  ```python
  transposee = matrice.T
  ```
* **🏷️ Label : `np.ravel`** (Aplatissement)  
  *Aplatit un tableau multidimensionnel en 1D. C'est plus efficace que `.flatten()` car cela renvoie une vue au lieu d'une copie.*
  ```python
  vecteur_1d = matrice.ravel()
  ```

<br>

---

<br>

#### Chapitre 8 : Données Manquantes (NaN)

Gérez efficacement les trous dans vos jeux de données.

* **🏷️ Label : Le piège de `np.nan`**  
  *> [!WARNING]  
  > `np.nan` (Not a Number) n'est jamais égal à lui-même. La comparaison `a == np.nan` renverra toujours `False`. Utilisez systématiquement `np.isnan(a)` pour détecter les valeurs manquantes.*
  ```python
  # CORRECT :
  masque_nan = np.isnan(a)
  ```
* **🏷️ Label : Tableaux Masqués (`np.ma.masked_array`)**  
  *Crée un tableau temporaire excluant les valeurs aberrantes ou NaN pour effectuer des calculs statistiques corrects sans effacer la donnée source.*
  ```python
  masked_a = np.ma.masked_array(a, np.isnan(a))
  ```

<br>

---

<br>

### 5. Ressources Supplémentaires 📚

Pour aller encore plus loin avec NumPy :
- 🔗 [Documentation officielle de NumPy](https://numpy.org/doc/stable/)
- 🔗 [Tutoriels interactifs sur W3Schools](https://www.w3schools.com/python/numpy_intro.asp)
- 🔗 [Cours express NumPy sur DataCamp](https://www.datacamp.com/community/tutorials/python-numpy-tutorial)

