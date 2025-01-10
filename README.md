# TP Note Clean Code BOUKADA Adel

Lien du projet : 
https://github.com/Leknif571/TpNoteCleanCode


# Spécification 
Puisque qu'aucun affichage n'as était demander, dans l'architecture du code seule les services et les modèles ont était garder.

Pour lancer les tests, il faut exécuter la commande suivante à la racine du projet :

Pour les tests unitaires :
```bash
py -m unittest discover -s tests/unit
```

Pour les tests fonctionnels :
```bash
py -m unittest discover -s tests/functional
```

Pour les tests de performance :
```bash
py -m unittest discover -s tests/performance
```

# Consigne

## Evaluation Clean Code / Tester son code
- Développer la proposition que vous voulez en TDD la plus complète possible
- Essayez de respecter au maximum les conseils de Clean Code vu durant la formation.
- Le projet à développer doit être en orienté objet dans le language de votre choix.
- Vous pouvez tout réaliser sans interaction dans la console ni interface (donc pour le jeu, en automatique ou statique (couleur placée par défaut par exemple))
- La notation se fera en deux parties (et sera probablement mixé, je verrai bien) :
    - Première partie : 
        - Sur la logique des tests en TDD (n'hésitez pas à numéroter vos tests si vous en changez l'ordre)
        - Sur le respect des règles du Clean Code (pensez à tout, du nom de vos variables, aux choses que font vos méthodes, à la bonne indentation etc...)
    - Seconde partie : 
        - Les tests mis en place :
            - Tests unitaires (tous les tests unitaires doivent être réalisés, mais si vous faites une TDD complète ce sera le cas)
            - Tests fonctionnels, au minimum deux tests fonctionnels : Remplir le board avec les couleurs et les couleurs sont dans le bon ordre + Réaliser un jeu complet du début à la fin. **OU** Une place de parking déjà réservée ne peut pas être à nouveau reservée + Réserver une place de parking, vérifier ce qu'il y a à vérifier et s'assurer qu'un tarif est appliqué (vous pouvez inventez le prix selon la durée à votre convenance)
            - Tests de performance : Réalisez deux tests de performances, pour tester les performances de ce que vous voulez
            - **Pensez à avoir un projet / dossier de test différent pour chaque type de test et respecter les normes de nommage des classes et de vos noms de tests**
- Le rendu se fait soit en zip avec NOM_PRENOM_TDD.zip ou via un lien github public qui me sera partagé sur discord (Cédric BRASSEUR / cbrasseur)
- Aucun Mock n'est demandé. Aucun autre type de tests n'est demandé (seulement unitaires, fonctionnels et )

## Proposition numéro 2 : Gestion de parking et stationnement d'un véhicule
### Interface / UI / UX
- Aucune interface n'est demandée, même concernant la console, aucun code n'est demandé en terme de Program.cs (main ou autre).

### Règles du parking
- Un parking avec X nombres de places
- Chaque place ne peut être reservée que par une voiture
- Les places libérées peuvent à nouveau être reservées

### Déroulement d'une reservation d'une place de parking
- Une voiture déja garée ne peut pas être à nouveau garée
- Une place ne peut avoir qu'une seule voiture garée
- A la fin de la reservation, la place est rendue et **un tarif est appliqué selon la durée du temps de parking**

### Attendu minimum niveau orienté objet
- Une classe pour gérer le parking
- Une classe pour gérer une place de parking (optionnelle mais sûrement intéressante)
- Une classe pour la voiture
- Autres classes possibles si vous l'estimez nécessaire
- **Pensez aux responsabilités de chaque classes**

## Les tests à réaliser
- Pensez à tous les tests à réaliser précisés en début de fichier
- Réalisez la TDD la plus complète que vous pouvez





