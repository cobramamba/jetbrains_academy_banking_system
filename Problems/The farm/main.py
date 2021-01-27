chicken = int(23)
goat = int(678)
pig = int(1296)
cow = int(3848)
sheep = int(6769)

money = int(input())

if sheep <= money:
    print(str(money // sheep) + " sheep")
elif cow <= money <= sheep:
    print(str(money // cow), "cow" if money // cow == 1 else "cows")
elif pig <= money < cow:
    print(str(money // pig), "pig" if money // pig == 1 else "pigs")
elif goat <= money < pig:
    print(str(money // goat), "goat" if money // goat == 1 else "goats")
elif chicken <= money < goat:
    print(str(money // chicken), "chicken" if money // chicken == 1 else "chickens")
else:
    print("None")
