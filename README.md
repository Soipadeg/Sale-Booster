# 📊 Sales Booster - Calculateur de Ventes par Heure

Un calculateur interactif pour optimiser vos **VpH** (Ventes par Heure) mobiles.

## 🚀 Installation

### Prérequis
- Python 3.8+
- pip

### Setup

```bash
# Installer les dépendances
pip install -r requirements.txt
```

## 📋 Utilisation

### Lancer l'application

```bash
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur sur `http://localhost:8501`

## 📌 Fonctionnalités

### Mode 1: Calculer votre VpH
- **Entrez:** Nombre d'heures de travail + Nombre de ventes mobiles
- **Obtenez:** Votre VpH (Ventes par Heure)
- **Formule:** `VpH = Ventes Mobiles / Heures de travail`

### Mode 2: Calculer les ventes à faire
- **Entrez:** Nombre d'heures de travail + VpH cible
- **Obtenez:** Nombre de ventes mobiles à réaliser
- **Formule:** `Ventes Mobiles = VpH Cible × Heures de travail`

## 📊 Exemple

**Mode 1:**
- Heures travaillées: 8h
- Ventes mobiles réalisées: 80
- **VpH obtenu: 10.00 ventes/heure**

**Mode 2:**
- Heures à travailler: 8h
- VpH cible: 10.00
- **Ventes mobiles à faire: 80**

## 🎨 Interface

- **2 onglets** pour les deux modes de calcul
- **Entrées numérotiques** pour une saisie facile
- **Résultats visuels** avec métriques colorées
- **Tableaux de comparaison** pour suivre vos données
- **Formules mathématiques** pour comprendre les calculs

## 📦 Structure

```
vph2000/
├── app.py              # Application principale
├── requirements.txt    # Dépendances
└── README.md          # Documentation
```

## 💡 Conseils d'utilisation

- Utilisez des **pas de 0.5h** pour les heures (flexible)
- Entrez les ventes mobiles en **nombres entiers**
- Comparez vos VpH entre différentes périodes
- Utilisez le Mode 2 pour fixer des **objectifs ambitieux**

## 📄 Licence

Libre d'utilisation
