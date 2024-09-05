def main():

    # recolter une valeur porte monnaie
    valeur1 = int(input("Entrer le montant du porte monnaie"))

    # creer un produit qui aura pour valeur 50
    valeur2 = 50

    # afficher la nouvelle valeur du porte monnaie, apres son achat
    result = (valeur1 - valeur2)

    # affiche le resultat
    print("Produit acheté !")
    print("La valeur du porte monnaie apres achat est de " + str(result))


if __name__ == '__main__':
    main()