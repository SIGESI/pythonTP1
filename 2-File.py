#création du fichier
def crer():
    nomFichier = str(input("Nom du fichier : "))
    fichier = open(nomFichier, "w+")
    fichier.close()

#écriture dans le fichier
def ecrire():
    nomFichier = str(input("Nom du fichier : "))
    fichier = open(nomFichier, "a")
    fichier.write("\n"+str(input("Entrez le texte : \n")))
    fichier.close()

#lecture du fichier
def lire():
    nomFichier = str(input("Nom du fichier : "))
    fichier = open(nomFichier, "r")
    print(fichier.read())
    fichier.close()

#vider le contenu du fichier
def vider():
    nomFichier = str(input("Nom du fichier : "))
    fichier = open(nomFichier, "w")
    fichier.close()

#Création du menu
def main():
    print("1. Choisir un nom de fichier ")
    print("2. Ajouter un texte")
    print("3. Afficher le fichier complet")
    print("4. Vider le fichier")
    print("9. Quitter")

    choix = 0

    while choix != 9:
        choix = int(input("Entrez votre choix : "))

        if choix == 1:
            crer()
        elif choix == 2:
            ecrire()
        elif choix == 3:
            lire()
        elif choix == 4:
            vider()
        elif choix == 9:
            exit()
        else:
            print("Choix non valide!")

if __name__ == '__main__':
    main()