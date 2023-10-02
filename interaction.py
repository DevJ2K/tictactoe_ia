import os
import typer
from tictactoe import *

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


home()