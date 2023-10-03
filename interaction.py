import os
import typer
from tictactoe import *
from entrainement_ia import *


def show_title(name, color, nbr_equals):
    os.system('clear')
    page = typer.style(name, fg=color)
    print(f"|{'#' * nbr_equals * 2 + '#' * len(name)}|")
    typer.echo(f"|{'=' * nbr_equals}{page}{'=' * nbr_equals}|")
    print(f"|{'#' * nbr_equals * 2 + '#' * len(name)}|")

def home():
    show_title("MENU", "yellow", 20)
    print("1. Affronter l'ia.")
    print("2. Entraîner l'ia.")
    print("3. Quitter.")
    choix = input("-> ")
    if choix == "1":
        start_game_menu()
    elif choix == "2":
        pass
    elif choix.lower() in ["3", "q", "quit"]:
        typer.secho("\nBye !", fg=typer.colors.BRIGHT_YELLOW)#, bg=typer.colors.YELLOW) 
        return
    else:
        home()




def play_game(player: int):
    reset_game()
    while True:
        if player == 1:
            statusUtilisateur = tour_utilisateur()
            if statusUtilisateur == True:
                gagnant = "player"
                break

            if statusUtilisateur == "tie":
                gagnant = "Egalité."
                break

            player = 2
        

        if player == 2:
            statusIA = tour_ia()
            if statusIA == True:
                gagnant = "ia"
                break

            if statusIA == "tie":
                gagnant = "Egalité."
                break
            player = 1

    if gagnant == "player":
        afficher_la_map("VICTOIRE DU JOUEUR", "bright_green", 12)
    elif gagnant == "ia":
        afficher_la_map("VICTOIRE DE L'IA", "bright_red", 13)
    else:
        afficher_la_map("EGALITE", "yellow", 13)
    save_game()
    input("(Appuyer sur Entrée pour revenir en arrière)")
    return home()

def start_game_menu():
    show_title("PARTIE CONTRE L'IA", "blue", 13)
    print("Qui commence ? :")
    print("1. Joueur.")
    print("2. Ia.")
    choix = input("-> ")
    if choix.lower() in ["q", "quit", "b", "back", "return"]:
        return home()
    elif choix not in ["1", "2"]:
        erreur = typer.style("Erreur !", fg="red")
        typer.echo(f"{erreur} Une valeur que vous avez entré est incorrecte.")
        input("(Appuyer sur Entrée pour recommencer)")
        return start_game_menu()
    return play_game(player=int(choix))


def learning(nombre_partie):
    show_title("APPRENTISSAGE EN COURS", "red", 9)
    ia_subit = nombre_partie // 2
    gagnant = None
    who_start = 1
    player = who_start

    #STATS
    victoire_ia = 0
    egalite_ia = 0
    nombre_partie_nouvelle = 0
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

def learning_menu():
    show_title("MACHINE LEARNING", "bright_magenta", 13)
    print("Combien de parties souhaitez-vous que l'IA fasse ?")
    choix = input("-> ")
    if choix.lower() in ["q", "quit", "b", "back", "return"]:
        return home()
    try:
        print("")
    except:
        erreur = typer.style("Erreur !", fg="red")
        typer.echo(f"{erreur} La valeur que vous avez entré n'est pas un nombre.")
        input("(Appuyer sur Entrée pour recommencer)")
        return learning_menu()

home()