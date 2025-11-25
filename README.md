# Projet de Cryptographie en Python

Ce projet présente différentes façons de chiffrer et sécuriser des données en Python. Il inclut des exemples d'implémentation de :

* **Zorlangue** (un chiffrement simple)
* **Code de César** (chiffrement par décalage)
* **Fernet** (cryptographie symétrique sécurisée avec la librairie `cryptography`)

---

## Table des matières

- [Projet de Cryptographie en Python](#projet-de-cryptographie-en-python)
  - [Table des matières](#table-des-matières)
  - [Prérequis](#prérequis)
  - [Installation](#installation)
  - [Méthodes de chiffrement](#méthodes-de-chiffrement)
    - [Zorlangue](#zorlangue)
    - [Code de César](#code-de-césar)
    - [Fernet](#fernet)
  - [Tests](#tests)
  - [Intégration continue (GitHub Actions)](#intégration-continue-github-actions)
  - [Licence](#licence)

---

## Prérequis

* Python 3.10+
* `pip` installé
* Environnement virtuel pour isoler les dépendances

---

## Installation

1. Crée un environnement virtuel :

```bash
python -m venv .venv
```

2. Active l'environnement :

* Sur Windows :

```bash
.venv\Scripts\activate
```

* Sur macOS/Linux :

```bash
source .venv/bin/activate
```

3. Installe les dépendances :

```bash
pip install -r requirements.txt
```

---

## Méthodes de chiffrement

### Zorlangue

Zorlangue est un chiffrement simple où l'ordre des lettres dans chaque mot est inversé.

---

### Code de César

Le code de César consiste à décaler chaque lettre d'un certain nombre de positions dans l'alphabet.

---

### Fernet

Fernet est une méthode de cryptographie symétrique sécurisée fournie par la librairie `cryptography`.

---

## Tests

Les tests sont réalisés avec `pytest`. Pour exécuter les tests :

```bash
pytest
```

---

## Intégration continue (GitHub Actions)
```

---

## Licence

Ce projet est sous licence MIT.
