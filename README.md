# BlockhainTP

Ce projet à été fait par : 

-Samuel FOTSO

-Presley Obiang

-Carnegie Beker MOMO


Dans ce projet, on a implémenté une simple chaîne de blocs (blockchain) en Python. Ce projet permet de comprendre les bases de la technologie blockchain, en particulier la structure des blocs et comment ils sont liés entre eux par des hachages cryptographiques.

-On a crée un fichier main.py, en suite importé hashlib pour pourvoir créer des messages cryptés à sens unique.

-Maintenant on créer une classe "Bloc" contient la méthode "__init__" (ou constructeur), qui est invoquée à chaque fois qu’un objet "Bloc" est créé.
La methode "__init__" a trois parèmetres {self (l’instance de chaque objet), hachage_bloc_precedent (une référence au bloc précédent), liste_transactions (une liste des transactions effectuées dans le bloc actuel)}.

-Un bloc contient plusieurs éléments : le hachage cryptographique du bloc précédent, une liste de transactions incluses dans ce bloc, une chaîne de caractères combinant les transactions et le hachage du bloc précédent, ainsi que le hachage "sha-256" de ces données.

-On a défini le constructeur de la classe "Bloc" pour initialiser ces attributs et générer le hachage du bloc.

-Ensuite, on a créé la classe "ChaineDeBlocs" pour représenter la chaîne de blocs entières.

-On a défini le constructeur de la classe "ChaineDeBlocs" pour initialiser la chaîne et générer le bloc de genèse(qui est le premier bloc). Le bloc de genèse n'a pas de prédécesseur, donc 

-on utilise "0" comme hachage du bloc précédent.
- La méthode "@property" est un accesseur en lecture pour l'attribut dernier_bloc de la classe "ChaineDeBlocs". Elle permet d'accéder au dernier bloc de la chaîne de blocs sans avoir à utiliser de parenthèses lors de l'appel.
- 
-On a également défini une méthode pour créer un nouveau bloc avec les transactions données et l'ajouter à la chaîne.

-Pour afficher les données et les hachages de chaque bloc de la chaîne, on a défini une méthode qui parcourt la chaîne de blocs et imprime les informations de chaque bloc.

-Enfin, on a ajouté une propriété pour retourner le dernier bloc de la chaîne. Cette propriété permet de simplifier l'accès au dernier bloc lorsque l'on veut ajouter un nouveau bloc à la chaîne.

