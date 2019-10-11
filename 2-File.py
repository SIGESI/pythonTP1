# les menus
def menu():
    print('--------------menu----------------')
    print("1. Choisir un nom de fichier")
    print("2. Ajouter un texte")
    print("3. Afficher le fichier complet")
    print("4. Vider le fichier")
    print("5. Quitter le programme")
    print('-------------menu----------------\n')

print('------------------------------')
print("      Fichier Application    ")
print('------------------------------\n')

a=1
while (a):
    menu()
    c = int(input(" Entrez votre choix de fonction:"))
    print(c)

    if c==1:
        print('------------Choisir un nom:------------------')
        print("a. fichierA")
        print("b. fichierB")
        print("c. fichierC")
        print('------------Choisir un nom------------------\n')
        nomChois=input(" Entrez votre choix de nom de ficher:")
        if nomChois == "a":
            nomFicher = "fichierA.txt"
        elif nomChois == "b":
            nomFicher = "fichierB.txt"
        elif nomChois == "c":
            nomFicher = "fichierC.txt"
        #ficher=open(nomFicher,"wt")
        #with open(nomFicher, "r") as ficher:
            print('nom de fichier est:',nomFicher)
        print('------------------------------\n')
    elif c==2:
        with open(nomFicher, "a+") as ficher:
        #ficher=open(nomFicher,"wt")
            texte=input("Ajouter un texte:")
            ficher.write(texte)
            print("Vous avez terminé d'ajouter")
        #ficher.close()
        print('------------------------------\n')
    elif c==3:
        with open(nomFicher, "r") as ficher:
            texteAfficher = ficher.read();
            print("Le contenu du fichier est: %s" % (texteAfficher))
        print('------------------------------\n')
    elif c== 4:
        with open(nomFicher, "r") as ficher:
            print("Le fichier a été vidé")
        print('------------------------------\n')
    elif c==5:
        a=0


