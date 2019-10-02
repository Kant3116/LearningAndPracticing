import random
nbr_secret = random.randint(0, 100)
mon_invite = "proposes un nombre : "
while True:
    nbr_joueur = int(input(mon_invite))
    if nbr_joueur == nbr_secret:
        print("Trouvé !!! ")
        break
    elif nbr_joueur > nbr_secret:
        print("Plus bas ! ")
    elif nbr_joueur < nbr_secret:
        print("Plus haut ! ")

print("trop fort !!")
