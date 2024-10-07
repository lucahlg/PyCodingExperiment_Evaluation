def triplets_with_sum(number):
    pass
    triplets = []
    # a und b durchgehen, wobei a < b und c = number - a - b
    for a in range(1, number // 3):  # a muss kleiner als number/3 sein
        for b in range(a + 1, number // 2):  # b muss kleiner als number/2 sein
            c = number - a - b
            if a**2 + b**2 == c**2:  # Pythagoras-Gleichung prüfen
                triplets.append((a, b, c))
    return triplets

# Beispiel:
number = 300
result = triplets_with_sum(number)
print("Pythagoreische Tripel bis N =", number)
for triplet in result:
    print(triplet)