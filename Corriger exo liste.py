from random_1 import shuffle

# Générateur de phrases
# demander en console une chaîne de la forme "mot1/mot2/mot3/mot4"
chained_words = input("entrer une chaine de la forme mot1/mot2/mot3/mot4")

# transformer cette chine en liste
words = chained_words.split("/")

# La mélanger
shuffle(words)

# récuperer le nombre d'éléments
words_len = len(words)

# Si le nombre d'éléments etst supérieur à 10
if words_len < 10:
    # afficher les 2 premiers mots
    print(words[0], words[1])

# Si le nombre délément est supérieur ou égal à 10
else:
    # Afficher les3 derniers mots
    print(words[words_len -1], words[words_len -2], words[words_len -3])