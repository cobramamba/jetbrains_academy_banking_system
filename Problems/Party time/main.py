guests = []

while True:
    name = input()

    if name == ".":
        break

    guests.append(name)

print(guests)
print(len(guests))
