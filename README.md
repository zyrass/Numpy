### Guide Complet sur NumPy 📚

NumPy (Numerical Python) est une bibliothèque fondamentale pour le calcul scientifique en Python. Elle fournit un support pour des tableaux de grandes dimensions et des matrices, ainsi qu'une collection de fonctions mathématiques pour les manipuler. Voici un guide détaillé pour comprendre et utiliser NumPy efficacement.

---

#### Sommaire

1. [Introduction à NumPy](#introduction-à-numpy)
2. [Installation de NumPy](#installation-de-numpy)
3. [Création et Manipulation des Tableaux](#création-et-manipulation-des-tableaux)
4. [Opérations sur les Tableaux](#opérations-sur-les-tableaux)
5. [Indexation et Slicing](#indexation-et-slicing)
6. [Fonctions Mathématiques](#fonctions-mathématiques)
7. [Manipulation de Forme](#manipulation-de-forme)
8. [Traitement de Données Manquantes](#traitement-de-données-manquantes)
9. [Bibliographie et Ressources](#bibliographie-et-ressources)

---

### Introduction à NumPy

NumPy est une bibliothèque pour le langage Python, ajoutant la prise en charge de tableaux et de matrices multidimensionnels, ainsi que des fonctions mathématiques de haut niveau pour opérer sur ces tableaux.

---

### Installation de NumPy

Pour installer NumPy, vous pouvez utiliser `pip` :

```bash
pip install numpy
```

---

### Création et Manipulation des Tableaux

#### Création de Tableaux

- **À partir d'une liste :**

```python
import numpy as np

a = np.array([1, 2, 3])
print(a)
```

- **Tableau de zéros :**

```python
zeros = np.zeros((2, 3))
print(zeros)
```

- **Tableau de uns :**

```python
ones = np.ones((2, 3))
print(ones)
```

- **Tableau vide (non initialisé) :**

```python
empty = np.empty((2, 3))
print(empty)
```

#### Propriétés des Tableaux

- **Dimension du tableau :**

```python
print(a.ndim)
```

- **Forme du tableau :**

```python
print(a.shape)
```

- **Type de données :**

```python
print(a.dtype)
```

- **Taille du tableau :**

```python
print(a.size)
```

- **Taille de chaque élément :**

```python
print(a.itemsize)
```

---

### Opérations sur les Tableaux

#### Opérations Arithmétiques

- **Addition :**

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)
```

- **Soustraction :**

```python
print(a - b)
```

- **Multiplication :**

```python
print(a * b)
```

- **Division :**

```python
print(a / b)
```

#### Fonctions Universelles

- **racine carrée :**

```python
print(np.sqrt(a))
```

- **exponentielle :**

```python
print(np.exp(a))
```

---

### Indexation et Slicing

- **Accès à un élément spécifique :**

```python
a = np.array([1, 2, 3, 4, 5])
print(a[2])
```

- **Slicing (portion de tableau) :**

```python
print(a[1:3])
```

- **Indexation par tableau booléen :**

```python
print(a[a > 2])
```

---

### Fonctions Mathématiques

- **Somme :**

```python
print(np.sum(a))
```

- **Produit :**

```python
print(np.prod(a))
```

- **Moyenne :**

```python
print(np.mean(a))
```

- **Médiane :**

```python
print(np.median(a))
```

- **Écart-type :**

```python
print(np.std(a))
```

---

### Manipulation de Forme

- **Changement de forme :**

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.reshape(3, 2))
```

- **Transposition :**

```python
print(a.T)
```

- **Aplatir un tableau :**

```python
print(a.ravel())
```

---

### Traitement de Données Manquantes

- **Masquer les valeurs manquantes :**

```python
a = np.array([1, 2, np.nan, 4])
masked_array = np.ma.masked_array(a, np.isnan(a))
print(masked_array)
```

- **Remplacer les valeurs manquantes :**

```python
a[np.isnan(a)] = 0
print(a)
```

---

### Bibliographie et Ressources

- [Documentation officielle de NumPy](https://numpy.org/doc/stable/)
- [Tutoriels NumPy sur W3Schools](https://www.w3schools.com/python/numpy_intro.asp)
- [Cours sur NumPy sur DataCamp](https://www.datacamp.com/community/tutorials/python-numpy-tutorial)

---

N'hésite pas à poser des questions pour approfondir certains points ou obtenir des explications supplémentaires sur des sujets spécifiques ! 😊