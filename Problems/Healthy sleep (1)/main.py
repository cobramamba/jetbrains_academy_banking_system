A = int(input())  # Sleep at least A hours a day
B = int(input())  # Sleep no more than B hours a day
H = int(input())  # Ann sleeps H hours a day

if B < H:
    print("Excess")
elif A <= H <= B:
    print("Normal")
else:
    print("Deficiency")
