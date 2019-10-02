# déclarer les variables en premier

pple = ["jean", "paul", "gauthier", "jean-jacques", "laura"]
chiffre = ["1", "2", "3", "4", "5"]
courses = ["eponge", "raviole", "champagne", "coke"]

# ici je declare quels elements je souhaite "printer" dans chaque index !

print(pple[1], chiffre[3], courses[3])

# je peux melanger les index pour créer une liste de listes

liste = [pple, chiffre, courses]
# ici je demande de printer l'élément num 2 de l'index num 1
print(liste[1][2])

a = len(pple)+len(chiffre)+len(courses)
if a > 20:
    print(a)
else:
    print("La condition pour printer a n'est pas remplie !")
# ici a = 15, la condition pour printer a n'est pas remplie
