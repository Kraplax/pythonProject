# Créer une liste qui va stocker des pseudos pour simuler un jeux online
# Kraplax, Vancy, Crata, Jestta ...
online_players = ["Kraplax", "Vancy", "Crata", "Jestta"]
print(online_players)
# Option 1 print(online_players)
# Option 2 print(online_players[x])
# Option 3 print(online_players[len(online_players) -x

# modifier 'Kraplax' -> 'Sierra11763'
online_players[0] = "Sierra11763"
online_players[2:4] = ["Paul", "Jacques"]
print(online_players)

# Insertion d'élement
online_players.insert(2, "Brave")
print(online_players)

# Ajouter en bout de liste
online_players.append("Nesquik")
online_players.extend(["kikoulol", "Roxor"])
print(online_players)

# Supprimer un joueuer
del online_players[7]
online_players.pop(6)
online_players.remove("Nesquik")
print(online_players)

# Clear la liste
del online_players[:]
online_players.clear()
print(online_players)