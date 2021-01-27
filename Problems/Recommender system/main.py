user_age = int(input())

if user_age > 60:
    print("Breakfast at Tiffany's")
elif 41 <= user_age <= 60:
    print("Pulp Fiction")
elif 26 <= user_age <= 40:
    print("Matrix")
elif 17 <= user_age <= 25:
    print("Trainspotting")
else:
    print("Lion King")
