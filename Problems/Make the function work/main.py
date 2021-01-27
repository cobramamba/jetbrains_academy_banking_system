def closest_higher_mod_5(x):
    while True:
        if x % 5 == 0:
            return x
        else:
            x += 1

# v = int(input())
# print(closest_higher_mod_5(v))
