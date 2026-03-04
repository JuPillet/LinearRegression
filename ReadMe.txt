I - English Version
II - Version Française

---
I - English Version
---

📝 Project Overview

This project serves as an introduction to the fundamental concepts of Machine Learning. The objective is to implement a simple linear regression algorithm to predict the price of a vehicle based on its mileage.

The project is divided into two main parts:

    Training: A program that reads a dataset and uses a gradient descent algorithm to optimize the model parameters (θ0​ and θ1​).

    Prediction: An interactive program that uses the trained parameters to estimate the price of a car after the user enters a mileage.

To run this project, you will be required to set up the environment using the provided script:

    Environment Initialization:
    Run the script for the first time to perform the installation:
    Bash

    ./pythenv3.sh

    Environment Activation:
    Relaunch it using the source command to enter the virtual environment:
    Bash

    source pythenv3.sh

    Exit the Environment:
    Once your work is finished, you can exit the environment with:
    Bash

    deactivate

📊 Features (Bonus)

The project also includes tools to validate the model's accuracy:

    Data Visualization: Displaying the dataset points on a graph.

    Regression Visualization: Displaying the prediction line overlaid on the data.

    Precision Calculation: A dedicated program to evaluate the reliability of the algorithm.

⚖️ Development Constraints

    The use of "turnkey" libraries (such as numpy.polyfit) is forbidden.

    Manual implementation of the gradient descent.

    Saving the thetas after training for immediate use by the predictor.

---
II - Version Française
---

ft_linear_regression
📝 Présentation du projet

Ce projet est une introduction aux concepts fondamentaux du Machine Learning. L'objectif est d'implémenter un algorithme de régression linéaire simple pour prédire le prix d'un véhicule en fonction de son kilométrage.

Le projet se décompose en deux parties principales :

    L'entraînement : Un programme qui lit un jeu de données et utilise l'algorithme de descente de gradient pour optimiser les paramètres du modèle (θ0​ et θ1​).

    La prédiction : Un programme interactif qui utilise les paramètres entraînés pour estimer le prix d'une voiture après la saisie d'un kilométrage par l'utilisateur.

Pour lancer ce projet, il vous sera demandé d'installer l'environnement via le script fourni :

    Initialisation de l'environnement :
    Exécutez une première fois le script pour l'installation :
    Bash

    ./pythenv3.sh

    Activation de l'environnement :
    Relancez-le ensuite avec la commande source pour entrer dans l'environnement virtuel :
    Bash

    source pythenv3.sh

    Quitter l'environnement :
    Une fois votre travail terminé, vous pouvez sortir de l'environnement avec :
    Bash

    deactivate

📊 Fonctionnalités (Bonus)

Le projet inclut également des outils pour valider la précision du modèle :

    Visualisation des données : Affichage des points du dataset sur un graphique.

    Visualisation de la régression : Affichage de la droite de prédiction superposée aux données.

    Calcul de précision : Un programme dédié pour évaluer la fiabilité de l'algorithme.

⚖️ Contraintes de développement

    Usage de bibliothèques "clés en main" (type numpy.polyfit) interdit.

    Implémentation manuelle de la descente de gradient.

    Sauvegarde des thétas après entraînement pour utilisation immédiate par le prédicteur.
