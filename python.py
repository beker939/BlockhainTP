import hashlib

# Crée des blocs
class Bloc:
    def __init__(self, hachage_bloc_precedent, liste_transactions):
        # On attribue la valeur du paramètre hachage_bloc_precedent à l'attribut d'instance self.hachage_bloc_precedent.
        self.hachage_bloc_precedent = hachage_bloc_precedent
        # On attribue la valeur du paramètre liste_transactions à l'attribut d'instance self.liste_transactions.
        self.liste_transactions = liste_transactions

        # Le hachage précédent et la liste de transactions sont stockés dans les données du bloc.
        self.donnees_bloc = f"{' - '.join(liste_transactions)} - {hachage_bloc_precedent}"
        # Le hachage du bloc est créé en utilisant "sha256" et le "hexdigest" c'est pour le mettre en héxadecimal.
        self.hachage_bloc = hashlib.sha256(self.donnees_bloc.encode()).hexdigest()

#  Répresente la chaine de bloc entière
class ChaineDeBlocs:
    def __init__(self):
        self.chaine = []
        self.generer_bloc_genese()

    def generer_bloc_genese(self):
        # On Génère et ajoute le bloc de genèse (le premier bloc de la chaîne).
        self.chaine.append(Bloc("0", ['Bloc de Genèse']))
    
    def creer_bloc_depuis_transactions(self, liste_transactions):
        # On récupère le hachage du dernier bloc pour créer un nouveau bloc.
        hachage_bloc_precedent = self.dernier_bloc.hachage_bloc
        # On crée un nouveau bloc avec les transactions données et l'ajoute à la chaîne.
        self.chaine.append(Bloc(hachage_bloc_precedent, liste_transactions))

    def afficher_chaine(self):
        # On affiche les données et les hachages de chaque bloc de la chaîne.
        for i in range(len(self.chaine)):
            print(f"Données {i + 1} : {self.chaine[i].donnees_bloc}")
            print(f"Hash {i + 1} : {self.chaine[i].hachage_bloc}\n")

    @property
    def dernier_bloc(self):
        # On retourne le dernier bloc de la chaîne.
        return self.chaine[-1]

# On crée des transactions
t1 = "Presley"
t2 = "Samuel"
t3 = "Carnegie"
t4 = "Python"
t5 = "Crypto"
t6 = "ChaîneDeBlocs"

# On initialiser la chaîne de blocs
ma_chaine_de_blocs = ChaineDeBlocs()

# On créer des blocs à partir des transactions
ma_chaine_de_blocs.creer_bloc_depuis_transactions([t1, t2])
ma_chaine_de_blocs.creer_bloc_depuis_transactions([t3, t4])
ma_chaine_de_blocs.creer_bloc_depuis_transactions([t5, t6])

# On afficher la chaîne de blocs
ma_chaine_de_blocs.afficher_chaine()
