import os
import random
import time
import typer
from read_game import deplacement



p = [" " for _ in range(9)]

deroulement_game = ""

gagnant = None
who_start = 1
player = who_start

def afficher_la_map():
    os.system("cls")
    print(" ___________ ")
    print("|           |")
    print("| {} | {} | {} |".format(p[0], p[1], p[2]))
    print("|-----------|")
    print("| {} | {} | {} |".format(p[3], p[4], p[5]))
    print("|-----------|")
    print("| {} | {} | {} |".format(p[6], p[7], p[8]))
    print("|___________|")
    

def utiliser(emplacement):
    if p[emplacement] != " ":
        return True
    return False 


def verifier_solution():
    if True in [ 
        #Horizontale
        p[0] == p[1] == p[2] != " ",
        p[3] == p[4] == p[5] != " ",
        p[6] == p[7] == p[8] != " ",
        #Verticale
        p[0] == p[3] == p[6] != " ",
        p[1] == p[4] == p[7] != " ",
        p[2] == p[5] == p[8] != " ",
        #Diagonale
        p[0] == p[4] == p[8] != " ",
        p[2] == p[4] == p[6] != " "
        ]:
        return True
    return False


def tour_utilisateur():
    global deroulement_game
    afficher_la_map()
    choix_joueur = int(input("Choisissez un nombre entre 1 et 9 : ")) - 1


    while utiliser(choix_joueur):
        afficher_la_map()
        print(f"L'emplacement {choix_joueur+1} est déjà utilisé !")
        choix_joueur = int(input("Choisissez un nombre entre 1 et 9 : ")) - 1

    p[choix_joueur] = typer.style("O", fg=typer.colors.BLUE)

    deroulement_game += f"A{choix_joueur+1}-"


    if verifier_solution(): #VICTOIRE DU JOUEUR
        deroulement_game += "L"
        return True

    if " " not in p:  #EGALITE
        deroulement_game += "E"
        return "tie"
    
    else:   #LE JEU CONTINUE
        return False



def tour_ia():
    global deroulement_game
    afficher_la_map()
    print(deroulement_game)
    choix_ordinateur = deplacement(deroulement_game=deroulement_game, who_start=who_start) - 1

    while utiliser(choix_ordinateur) and " " in p:
        afficher_la_map()
        choix_ordinateur = deplacement(deroulement_game=deroulement_game, who_start=who_start) - 1

    p[choix_ordinateur] = typer.style("X", fg=typer.colors.RED)
    deroulement_game += f"I{choix_ordinateur+1}-"


    if verifier_solution(): #VICTOIRE DE L'IA
        deroulement_game += "W"
        return True

    if " " not in p:  #EGALITE
        deroulement_game += "E"
        return "tie"

    else:   #LE JEU CONTINUE
        return False


while True:

    if player == 1:
        statusUtilisateur = tour_utilisateur()
        if statusUtilisateur == True:
            gagnant = "Victoire du joueur."
            break

        if statusUtilisateur == "tie":
            gagnant = "Egalité."
            break

        player = 2
    

    if player == 2:
        statusIA = tour_ia()
        if statusIA == True:
            gagnant = "Victoire de l'IA."
            break

        if statusIA == "tie":
            gagnant = "Egalité."
            break
        player = 1

afficher_la_map()
print(gagnant)


# print(deroulement_game)

################################################
#Recupere les games dans 'cerveau_ia.txt' et est capable de reconstituer une partie.

#A = Celui qui commence
#I = Le suivant

#Si la sauvegarde commence par A, ça signifie que c'est l'utilisateur qui a commencé, sinon c'est l'IA

#Si la sauvegarde termine par L, c'est une défaite à ne pas reproduire, sinon c'est une Win sur laquelle l'IA peut se baser pour la reproduire, ou une Egalité si c'est E

#RECUPERER TOUTES LES GAMES
with open("cerveau_ia.txt", "r") as f:
    all_games = f.read().splitlines()


#SAUVEGARDER LA GAME
with open("cerveau_ia.txt", "a") as f:
    if deroulement_game not in all_games:
        if who_start == 1:
            f.write("\n"+deroulement_game)
            print("Nouvelle apprentissage !")

        if who_start == 2:
            if deroulement_game.endswith("W"):
                deroulement_game = deroulement_game.replace("W", "L")
            elif deroulement_game.endswith("L"):
                deroulement_game = deroulement_game.replace("L", "W")

            deroulement_game = deroulement_game.replace("A", "X").replace("I", "A").replace("X", "I")
            if deroulement_game not in all_games:
                f.write("\n"+deroulement_game)
                print("Nouvelle apprentissage !")

        
