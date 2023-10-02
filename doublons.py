with open("cerveau_ia.txt", "r") as f:
    all_games = f.read().splitlines()
    for i in all_games:
        if all_games.count(i) > 1:
            print(i)