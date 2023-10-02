import random
import os

deroulement_game = "A1-"

#RECUPERER TOUTES LES GAMES
with open("cerveau_ia.txt", "r") as f:
    all_games = f.read().splitlines()


# #SAUVEGARDER LA GAME
# with open("cerveau_ia.txt", "a") as f:
#     if deroulement_game not in all_games:
#         f.write("\n"+deroulement_game)




def deplacement(deroulement_game, who_start=1) -> int:
    game_potentiels = []

    game_a_suivre = ""
    prochain_deplacement = ""

    game_gagnante_a_suivre = ""
    game_egalite_a_suivre = ""
    game_perdante_a_suivre = ""

    if who_start == 1:
        # print(deroulement_game[6:8])
        if len(deroulement_game) == 3:
            if deroulement_game.startswith("A1-") or deroulement_game.startswith("A3-") or deroulement_game.startswith("A7-") or deroulement_game.startswith("A9-"):
                return 5
            


        else:
            game_potentiels = [game for game in all_games if game.startswith(deroulement_game)]
        


    elif who_start == 2:
        deroulement_game = deroulement_game.replace("A", "X").replace("I", "A").replace("X", "I")
        game_potentiels = [game for game in all_games if game.startswith(deroulement_game)]
        # print(deroulement_game)
        
        for i in range(len(game_potentiels)):
            if game_potentiels[i].endswith("W"):
                game_potentiels[i] = game_potentiels[i].replace("W", "L")
            elif game_potentiels[i].endswith("L"):
                game_potentiels[i] = game_potentiels[i].replace("L", "W")

        # print(game_potentiels)

    game_gagnantes = [i for i in game_potentiels if i.endswith("W")]
    game_perdantes = [i for i in game_potentiels if i.endswith("L")]
    game_egalites = [i for i in game_potentiels if i.endswith("E")]


    # TOUTES LES GAMES AYANT EU LIEU AVEC CE DEBUT DE PARTIE
    # print("Gagnantes : "+ str(game_gagnantes))
    # print("Perdantes : "+ str(game_perdantes))
    # print("Egalites : "+ str(game_egalites))


    
    if game_gagnantes != []: #S'il existe des games gagnantes avec ce début.
        # print("Ca a marché une fois, pourquoi pas 2 ?")
        plus_petit_game = random.choice(game_gagnantes)
        for game in game_gagnantes:
            if len(game) < len(plus_petit_game):
                plus_petit_game = game

        game_gagnante_a_suivre = plus_petit_game



    if game_egalites != []:
        plus_petit_game = random.choice(game_egalites)
        for game in game_egalites:
            if len(game) < len(plus_petit_game):
                plus_petit_game = game

        game_egalite_a_suivre = plus_petit_game



    if game_perdantes != []: #S'il a déjà perdu des games, se baser sur ces dernières pour ne pas produire les mêmes erreurs.
        # print("J'ai jamais gagné avec ce début de game, je vais me baser sur mes défaites pour avancer...")
        # print(game_perdantes)

        plus_petit_game = random.choice(game_perdantes)
        for game in game_perdantes:
            if len(game) < len(plus_petit_game):
                plus_petit_game = game
        
        game_perdante_a_suivre = plus_petit_game


    if game_gagnante_a_suivre != "" and game_perdante_a_suivre != "":
        if who_start == 1:
            if len(game_gagnante_a_suivre) > len(game_perdante_a_suivre):   #Si la victoire nécessite plus d'étapes de la défaite -> DEFENDRE
                prochain_deplacement = game_perdante_a_suivre[len(deroulement_game)+4:len(deroulement_game)+5]

            elif len(game_gagnante_a_suivre) < len(game_perdante_a_suivre): #Sinon -> ATTAQUE
                prochain_deplacement = game_gagnante_a_suivre[len(deroulement_game)+1:len(deroulement_game)+2]

            else:
                prochain_deplacement = game_egalite_a_suivre[len(deroulement_game)+1:len(deroulement_game)+2]
        

        elif who_start == 2:
            if len(game_gagnante_a_suivre) > len(game_perdante_a_suivre):   #Si la victoire nécessite plus d'étapes de la défaite -> DEFENDRE
                prochain_deplacement = game_perdante_a_suivre[len(deroulement_game)+4:len(deroulement_game)+5]

            elif len(game_gagnante_a_suivre) < len(game_perdante_a_suivre): #Sinon -> ATTAQUE
                prochain_deplacement = game_gagnante_a_suivre[len(deroulement_game)+1:len(deroulement_game)+2]

            else:
                prochain_deplacement = game_egalite_a_suivre[len(deroulement_game)+1:len(deroulement_game)+2]

    elif game_gagnante_a_suivre == "" and game_perdante_a_suivre != "":
        # print("HERE")
        prochain_deplacement = game_perdante_a_suivre[len(deroulement_game)+4:len(deroulement_game)+5]

    elif game_gagnante_a_suivre != "" and game_perdante_a_suivre == "":
        prochain_deplacement = game_gagnante_a_suivre[len(deroulement_game)+1:len(deroulement_game)+2]

    
    elif (game_gagnante_a_suivre == game_perdante_a_suivre == "") and game_egalite_a_suivre != "":
        prochain_deplacement = game_gagnante_a_suivre[len(deroulement_game)+1:len(deroulement_game)+2]

    elif game_gagnante_a_suivre == game_perdante_a_suivre == game_egalite_a_suivre == "":
        prochain_deplacement = random.randint(1, 9)
    

    # ####################################################################################
    # if game_gagnante_a_suivre != "" and game_perdante_a_suivre != "":
    #     if len(game_gagnante_a_suivre) > len(game_perdante_a_suivre) or (len(game_gagnante_a_suivre) == len(game_perdante_a_suivre) and who_start == 1):
    #         prochain_deplacement = game_perdante_a_suivre[len(deroulement_game)+4:len(deroulement_game)+5]
        
    #     elif len(game_gagnante_a_suivre) < len(game_perdante_a_suivre) or (len(game_gagnante_a_suivre) == len(game_perdante_a_suivre) and who_start == 2):
    #         prochain_deplacement = game_gagnantes[len(deroulement_game)+1:len(deroulement_game)+2]


    # elif game_gagnante_a_suivre == "" and game_perdante_a_suivre != "":
    #     prochain_deplacement = game_perdante_a_suivre[len(deroulement_game)+4:len(deroulement_game)+5]


    # elif game_gagnante_a_suivre != "" and game_perdante_a_suivre == "":
    #     prochain_deplacement = game_gagnantes[len(deroulement_game)+1:len(deroulement_game)+2]
    # ####################################################################################
            

    # print(game_gagnante_a_suivre, game_perdante_a_suivre, game_egalite_a_suivre)

    if prochain_deplacement == "":
        prochain_deplacement = random.randint(1, 9)

    # print("Prochain déplacement -> " + str(prochain_deplacement))
        
    return int(prochain_deplacement)


os.system("cls")
for i in range(5):
    deplacement(deroulement_game=deroulement_game)