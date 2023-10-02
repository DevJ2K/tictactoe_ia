import os
import random
import time
import typer
from read_game import deplacement


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
    
    choix_joueur = random.randint(0, 8)

    while utiliser(choix_joueur) and " " in p:
        
        choix_joueur = deplacement(deroulement_game=deroulement_game, who_start=who_start) - 1

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
    
    choix_ordinateur = deplacement(deroulement_game=deroulement_game, who_start=who_start) - 1

    while utiliser(choix_ordinateur) and " " in p:
        
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


def lancer_partie(player):
    global gagnant
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



def sauvegarder_la_partie():
    global deroulement_game, nombre_partie_nouvelle
    #RECUPERER TOUTES LES GAMES
    with open("cerveau_ia.txt", "r") as f:
        all_games = f.read().splitlines()


    #SAUVEGARDER LA GAME
    with open("cerveau_ia.txt", "a") as f:
        if deroulement_game not in all_games:
            if who_start == 1:
                f.write("\n"+deroulement_game)
                nombre_partie_nouvelle += 1

            if who_start == 2:
                if deroulement_game.endswith("W"):
                    deroulement_game = deroulement_game.replace("W", "L")
                elif deroulement_game.endswith("L"):
                    deroulement_game = deroulement_game.replace("L", "W")

                deroulement_game = deroulement_game.replace("A", "X").replace("I", "A").replace("X", "I")
                if deroulement_game not in all_games:
                    f.write("\n"+deroulement_game)
                    nombre_partie_nouvelle += 1




p = [" " for _ in range(9)]

deroulement_game = ""

gagnant = None
who_start = 1
player = who_start



#PARAMETRES
nombre_partie = 200
ia_subit = nombre_partie // 2


#STATS
victoire_ia = 0
egalite_ia = 0
nombre_partie_nouvelle = 0

print("Apprentissage en cours...")

with typer.progressbar(range(nombre_partie)) as progress:
    for i in progress:

        #Rénitialiser la game
        p = [" " for _ in range(9)]
        deroulement_game = ""
        player = who_start
        gagnant = None

        if i == ia_subit:
            who_start = 2
            player = who_start

        lancer_partie(player=who_start)
        
        # time.sleep(0.5)
        if gagnant == "Victoire de l'IA.":
            victoire_ia += 1
        elif gagnant == "Egalité.":
            egalite_ia += 1

        sauvegarder_la_partie()
        # afficher_la_map()
        # print(gagnant)

# lancer_partie(player=2)


# afficher_la_map()
# print(gagnant)
print(f"Stats de l'IA : [{nombre_partie} Parties]\nVictoire -> {victoire_ia} | Egalité -> {egalite_ia} | Défaite -> {nombre_partie-(victoire_ia+egalite_ia)}")
print(f"L'IA a gagné {(100*victoire_ia)//nombre_partie}% de ses parties.")
print(f"L'IA a appris {nombre_partie_nouvelle} nouvelles parties !")
# sauvegarder_la_partie()



        
