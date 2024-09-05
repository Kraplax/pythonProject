# Système de Place de cinéma

# Récolter l'âge de la personne "Quel et votre age ?"
age = int(input("Quel âge avez-vous ?"))

# Si la personne est mineur -> 7€
#if age < 18:
    #prix_total = 7

# Si la personne est majeur -> 12€
#else:
    #prix_total = 12

# Condition Ternaire (attention a (><)
prix_total = (7, 12)[age > 18]

# Souhaitez-vousdu pop corn ?
request_pop_corn = input("Voulez-vous du pop corn ? (Oui, Non)")

# Si oui -> +5€
if request_pop_corn == "Oui":
    prix_total += 5

# Afficher ce prix total à payer
print("Vous devez payer", prix_total, "€")