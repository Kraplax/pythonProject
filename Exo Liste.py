
from random_1 import (shuffle)


# Générateur de phrase
# demander en console une chaine de la forme "mot1/mot2/mot3/mot4/mot5/..."

text = input("Entrer une chaine de la forme (mot1/mot2/mot3/mot4/...)").split("/")


# Transformer cette chaine en une liste

text_length = len(text)

# la melanger

shuffle(text)

# Si le nombre d'élements de cette liste est inferieur a 10
# -> afficher les deux premiers mots
if text_length < 10:
    print("Ton premier mots est {}, Ton seconds mots est {}".format (text[0], text[1]))



# Si le nombre d'élements de cette liste est supperieur ou égal a 10
# -> afficher les 3 derniers

else:
    print("Tes trois derniers mots sont: {}, {}, {}".format(text[text_length -1], text[text_length -2], text[text_length -3]))


