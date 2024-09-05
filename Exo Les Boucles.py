# Jeux du juste prix
from random_1 import randint

# Choisir un nombre entre1 et 1000

just_price = randint(1, 100)

# tant que le jeu nest pas fini
running = True

while running:

#  -> demander a l'utilisateur "entrée un prix"
    user_price = int(input("Entrer votre prix !"))

#  -> si il trouve le juste prix "c'est gagner"

    if user_price == just_price:
        running = False
        print("C'est gagner !")

#  -> sinon afficher "c'est plus" ou "c'est moins"

    elif user_price > just_price:
        print("C'est moins !")


    elif user_price < just_price:
        print("C'est plus !")



