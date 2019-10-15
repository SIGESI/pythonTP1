#création du fichier
def crer():
    while True:
        try:
            nomFichier = str(input("Nom du fichier : "))
            fichier = open(nomFichier, "w+")
        except OSError as err:
            print("OS error: {0}".format(err))
        else:
            fichier.close()
            print("you have created the fichier")
            break

#écriture dans le fichier
def ecrire():
    while True:
        try:
            nomFichier = str(input("Nom du fichier : "))
            fichier = open(nomFichier, "a")
            fichier.write("\n" + str(input("Entrez le texte : \n")))
        except OSError as err:
            print("OS error: {0}".format(err))
        else:
            fichier.close()
            break


#lecture du fichier
def lire():
    while True:
        try:
            nomFichier = str(input("Nom du fichier : "))
            fichier = open(nomFichier, "r")
            print(fichier.read())
        except OSError as err:
            print("OS error: {0}".format(err))
        else:
            fichier.close()
            break

#vider le contenu du fichier
def vider():
    while True:
        try:
            nomFichier = str(input("Nom du fichier : "))
            fichier = open(nomFichier, "w")
        except OSError as err:
            print("OS error: {0}".format(err))
        else:
            fichier.close()
            break

#Création du menu
def main():
    print("1. Choisir un nom de fichier ")
    print("2. Ajouter un texte")
    print("3. Afficher le fichier complet")
    print("4. Vider le fichier")
    print("9. Quitter")

    choix = 0

    while choix != 9:

        while True:
            try:
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
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again   ")
            finally:
                print("------------------")


if __name__ == '__main__':
    main()

