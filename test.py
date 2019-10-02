import random
while True:
    exit_or_not = input("Do you wish to continue ? ")
    aff = "yes"
    neg = "no"
    proposition = "Quel est le bon nombre ? "
    nbre_secret_no2 = random.randint(0, 100)
    while True:
        nombre_choisis = int(input(proposition))
        if nombre_choisis < nbre_secret_no2:
            print("Vers le ciel !!!")
        elif nombre_choisis > nbre_secret_no2:
            print("Vers les abysses !!")
        elif nbre_secret_no2 == nombre_choisis:
            print("Bienvenue sur Terre !!")
            break
    if
pass
