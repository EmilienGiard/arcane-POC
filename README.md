# arcane-POC

#### L'étude de cas réaliser dans le cadre de ma candidature pour Arcane. L'objectif est de créer un microservice avec une API REST qui permet aux utilisateurs de réaliser toutes les fonctionnalités citées ci-dessous.

## Features

Un utilisateur peut modifier les caractéristiques d’un bien (changer le nom, ajouter une pièce, etc… )

Les utilisateurs peuvent renseigner/modifier leurs informations personnelles sur la plateforme (nom, prénom, date de naissance)

Les utilisateurs peuvent consulter uniquement les biens d’une ville particulière

Un propriétaire ne peut modifier que les caractéristiques de son bien sans avoir accès à l’édition des autres biens.

# Prérequis

## Docker

### Linux

Lancer les commandes ci-dessous:

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install -y docker-ce
```

### Mac

Installer l'application docker:
```
https://docs.docker.com/engine/installation/#supported-platforms
```

## Docker-compose

### Linux

Lancer les commandes ci-dessous:

```
sudo curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Vous pouvez tester l'installation avec:

```
docker-compose --version
```

### Mac

Inclus dans l'application docker

# Installation

Run:
```
npm run server:install
npm run db:upgrade
```

# Utilisation

```
npm run server:run
```

Les routes disponibles sont:

```
http://0.0.0.0:5000/arcane-poc/user
http://0.0.0.0:5000/arcane-poc/town
http://0.0.0.0:5000/arcane-poc/town/id
http://0.0.0.0:5000/arcane-poc/property
```
