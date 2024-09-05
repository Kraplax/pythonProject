# Système de Place de cinéma

# Récolter l'âge de la personne "Quel et votre age ?"
age = int (input("Quel est votre âge ?"))

# Si la personne est mineur -> 7€
if age < 18:
    prix_total = 7

# Si la personne est majeur -> 12€
else:
    prix_total = 12

# Souhaitez-vousdu pop corn ?
pop_corn_request = input("Souhaitez-vous du pop corn ? (Oui, Non)")

# Si oui -> +5€
if pop_corn_request == "Oui":
    prix_total += 5

# Afficher ce prix total à payer
print("Vous devez payer", prix_total, "€")