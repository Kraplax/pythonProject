
# un youtubeur "krapinou", 2500 abonnés
suscribers_count = 2500

# il gagne 10% d'audience supplementairepar mois
months = 0

# on souhaite estimer, combien aura t'il d'abonner dans 2ans (24 mois)
while months <= 24:

   # augmenter l'audiance
   # + 30% : 1 + (30/100) : 1.3
   # - 20% : 1 - (20/100) : 0.8
   suscribers_count *= 1.10

   # Afficher le nombre d'abonnés
   print("Vous avais actuellement {} abonnés !".format(suscribers_count))

   # passer au mois suivant
   months += 1

