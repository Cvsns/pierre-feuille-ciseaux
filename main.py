import random

while True:
    user = input("Veuillez choisir pierre, feuille ou ciseaux : ").lower()
    print("Vous avez fait votre choix.")
    pc = random.choice(["pierre", "feuille", "ciseaux"])
    print("L'ordinateur a fait son choix : " + pc)
    if user == pc:
        print("Égalité !")
    elif (user == "pierre" and pc == "ciseaux") \
            or (user == "feuille" and pc == "pierre") \
            or (user == "ciseaux" and pc == "feuille"):
        print("Vous avez gagné !")
    else:
        print("Vous avez perdu !")
    reponse = input("Voulez-vous rejouer ? (oui/non) : ")
    if reponse.lower() not in ["oui", "o"]:
        break
