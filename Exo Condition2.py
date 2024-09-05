# Achat d'ordinateur


# Verifier le solde du compte
wallet = int(input("Entrer le solde de votre compte"))

# Recolter le prix de l'ordinateur
computeur_price = 1200

# Acheter ou non l'ordinateur
if wallet >= computeur_price:
    request_gift_paper = input("Voulez-vous un papier cadeaux ? (Oui, Non)")
    if request_gift_paper == "Oui":
        computeur_price += 20
    print("produit acheter !")
    print("Vous avez acheté l'ordinateur avec succès. Il vous reste ", str(wallet - computeur_price), "€")

else:
    print("Sale pauvre !")
    print("Va travailler !")




