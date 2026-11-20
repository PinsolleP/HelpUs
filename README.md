# HelpUs – Échange de compétences

## 1. Présentation du projet

**HelpUs** est une application web développée avec Django.

Le projet a pour objectif de faciliter l'échange de compétences entre particuliers. Il permet à des personnes de proposer leur savoir-faire et d'apporter leur aide à d'autres personnes souhaitant réaliser une activité pour laquelle elles ne disposent pas des compétences nécessaires.

L'application repose sur un principe d'entraide et de partage de connaissances, en mettant en relation les personnes selon leurs compétences et leurs disponibilités.

### Objectifs

- Permettre aux utilisateurs de proposer leurs compétences.
- Permettre aux utilisateurs de rechercher une aide pour une activité.
- Faciliter la mise en relation entre les personnes.
- Gérer les disponibilités pour organiser les échanges.
- Proposer une interface accessible aux visiteurs et aux utilisateurs connectés.

## 2. Fonctionnalités

### Visiteur
- Consulter les compétences proposées sur la plateforme.
- Consulter les prochaines propositions d'aide de manière anonyme.

### Utilisateur connecté
- Créer un compte et se connecter.
- Consulter et sélectionner les compétences disponibles.
- Indiquer les compétences qu'il possède et souhaite partager.
- Publier des activités pour lesquelles il recherche de l'aide.
- Gérer ses disponibilités.
- Consulter les demandes d'aide correspondant à ses compétences.
- Se proposer pour aider un autre utilisateur.

### Administration
- Gérer les utilisateurs.
- Gérer les compétences.
- Gérer les activités et les publications.
- Gérer les disponibilités.

## 3. Périmètre du prototype

Cette première version constitue un prototype fonctionnel.

Certaines fonctionnalités envisagées dans le sujet initial ne sont pas intégrées :
- Recherche géographique et proximité des utilisateurs.
- Prise en compte des conditions météorologiques.
- Gestion des créneaux horaires précis : les disponibilités sont considérées sur une journée entière.

## 4. Environnement technique

| Technologie | Utilisation |
|---|---|
| Python 3.13 | Langage de programmation |
| Django 5.2 | Framework web |
| SQLite | Base de données |
| HTML5 | Structure des pages |
| CSS3 | Mise en forme |
| Bootstrap | Framework CSS |
| PyCharm | Environnement de développement |
| Git | Gestion de versions |
| GitHub | Hébergement du projet |

## 5. Installation et configuration

### Prérequis
- Python 3.13
- Git
- Un environnement de développement Python

### Récupération du projet

```bash
git clone URL_DU_DEPOT
cd HelpUs
```

### Création de l'environnement virtuel

```bash
python -m venv venv
```

### Activation de l'environnement virtuel

Sous Windows :

```powershell
venv\Scripts\activate
```

### Installation de Django

```bash
pip install Django==5.2.18
```

### Initialisation de la base de données

```bash
python manage.py migrate
```

### Création d'un compte administrateur

```bash
python manage.py createsuperuser
```

### Lancement du serveur de développement

```bash
python manage.py runserver
```

L'application est ensuite accessible à l'adresse :

http://127.0.0.1:8000/

## 6. Architecture du projet

L'application repose sur une architecture Django organisée autour d'un projet principal et d'une application unique.

Les différentes responsabilités sont réparties entre :
- **Models** : gestion des données et relations entre les entités.
- **Views** : traitement des requêtes et logique applicative.
- **Templates** : affichage des pages HTML.
- **URLs** : gestion du routage de l'application.
- **Forms** : gestion et validation des formulaires.

## 7. Gestion du projet

Le développement est réalisé à l'aide de Git afin de suivre les évolutions du code et de conserver un historique des modifications.

Les bonnes pratiques mises en œuvre comprennent :
- Utilisation d'un environnement virtuel dédié.
- Programmation orientée objet.
- Organisation et séparation des responsabilités.
- Utilisation de conventions de nommage en anglais.
- Documentation du code avec des docstrings.
- Gestion des versions avec Git.

## 8. Contexte de réalisation

Projet réalisé individuellement dans le cadre d'une évaluation de développement web Python, sur une durée de trois jours.

**Formation :** Préparation au titre professionnel Concepteur Développeur d'Applications (CDA).