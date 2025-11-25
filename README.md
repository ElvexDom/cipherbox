# Projet de Cryptographie en Python

Ce projet présente différentes façons de chiffrer et sécuriser des données en Python. Il inclut des exemples d'implémentation de :

* **Zorlangue** (un chiffrement simple)
* **Code de César** (chiffrement par décalage)
* **Fernet** (cryptographie symétrique sécurisée avec la librairie `cryptography`)

---

## Table des matières

* [Prérequis](#prérequis)
* [Installation](#installation)
* [Lancer l'application](#lancer-lapplication)
* [Méthodes de chiffrement](#méthodes-de-chiffrement)

  * [Zorlangue](#zorlangue)
  * [Code de César](#code-de-césar)
  * [Fernet](#fernet)
* [Tests](#tests)
* [Intégration continue (GitHub Actions)](#intégration-continue-github-actions)
* [Licence](#licence)

---

## Prérequis

* Python 3.11+
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

## Lancer l'application

Depuis la racine du projet, lance le module principal avec :

```bash
python -m application
```

**Exemple d’utilisation :**

1. L’interface affichera un menu pour choisir le type de chiffrement.
2. Saisis le texte à chiffrer.
3. Choisis l’option de chiffrement souhaitée (Zorlangue, César, ou Fernet).
4. Visualise le texte chiffré et, si disponible, le texte déchiffré.

> ⚠️ Assure-toi d’avoir activé l’environnement virtuel avant d’exécuter le programme.

---

## Méthodes de chiffrement

### Zorlangue

Zorlangue est un chiffrement simple où l'ordre des lettres dans chaque mot est inversé.

### Code de César

Le code de César consiste à décaler chaque lettre d'un certain nombre de positions dans l'alphabet.

### Fernet

Fernet est une méthode de cryptographie symétrique sécurisée fournie par la librairie `cryptography`.

---

## Tests

Les tests sont réalisés avec `pytest`. Pour exécuter les tests depuis la racine du projet :

```bash
pytest tests
```

* Tu peux exécuter tous les tests ou un fichier spécifique :

```bash
pytest tests/test_console_ui.py
```

* Pour voir les détails de chaque test :

```bash
pytest -v
```

---

## Intégration continue (GitHub Actions)

Exemple d’étapes pour CI :

```yaml
- name: Run all unit tests
  run: pytest tests
```

---

## Licence

Ce projet est sous licence MIT.
