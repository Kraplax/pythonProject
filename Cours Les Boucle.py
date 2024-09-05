print("Vous êtes le client n°1")
print("Vous êtes le client n°2")
print("Vous êtes le client n°3")
print("Vous êtes le client n°4")
print("Vous êtes le client n°5")

# for : pour une valeur de départ (1) jusqu'à une valeur d'arrivé (5)
for num_client in range(1, 6):
   print("Vous êtes le client n°", num_client)

   # for each :pour chaque valeur d'une liste données
   print("Email envoyé à : kraplax@gmail.com")
   print("Email envoyé à : kraplax@kraplax.fr")
   print("Email envoyé à : contact@kraplax.fr")

# Lister les email

emails = ['krapalx@gmail.com', 'kraplax@kraplax.fr', 'contact@kraplax.fr']

# pour chaqu'une des valeur, j'affiche email envoyé à [INSERE EMAIL]

for email in emails:

   if email in blacklist:

      print("Email {} interdit !  envoi impossible ...".format(email))
      continue
      #break

   print("Email est envoyé à : ", email)

# while : tant qu'une condition est vrai
# salarié 1500€/ mois

salary = 1500

# tant que le salaire et <2000€, +120€

while salary < 10000:
   # ajoute 120€
   salary += 120
   # Affice le resultat
   print("Votre salaire actuel est de ", salary, "€")

print("Fin du programme")
