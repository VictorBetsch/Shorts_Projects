import random


def flip():
    chance = random.randint(0, 1)
    if chance == 0:
        return "pile"
    else:
        return "face"


money = 200


while 0 <= money <= 500:
    print("Vous avez ", money, "€")
    mise = int(input("Combien voulez-vous miser? "))
    choice = input("pile ou face ? ")
    piece = flip()
    print(piece)
    if choice == piece:
        print("Vous avez gagné", mise)
        money += mise
    else :
        print("Vous avez perdu", mise)
        money -= mise

if money <= 0:
    print("Vous n'avez plus d'argent")
elif money >= 500:
    print("Bien joué! Vous avez gagné!")
