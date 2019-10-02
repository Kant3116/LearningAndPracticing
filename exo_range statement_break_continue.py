People = ["Jong", "Yacine", "Francis", "Pierre"]
for p in range(len(People)):
    print(p, People[p])
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("found a shity number:", num)
