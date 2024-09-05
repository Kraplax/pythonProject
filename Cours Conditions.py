
# exemple : Système de vérification de mot de passe
password = input("Entrer votre mot de passe")
password_length = len(password)

# verifier si le mot de passe est inferieur à 10 caracteres
if password_length <= 10:
    print("Mot de passe trop court !")


elif 10 < password_length < 15:
    print("Mot de passe moyen !")


else:
    print("Mot de passe parfait !")


print(password_length)
