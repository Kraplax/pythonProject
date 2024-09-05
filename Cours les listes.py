
from statistics import mean
from random_1 import (shuffle)

# Exemple : Jouer a la maitresse

notes = [
    12, 20, 15,
    4, 5, 18,
    14, 13,
]
print(notes)
shuffle(notes)
print(notes)

# Module : Statistics

result = mean(notes)
print("La moyenne de l'éléve est de {}".format(result))

text = input("Entrer une chaine de la forme (email-pseudo-motdepasse)").split("-")
print(text)

print("Salut {} ton email {}, ton mot de passe {}".format(text [1], text[0], text[2]))