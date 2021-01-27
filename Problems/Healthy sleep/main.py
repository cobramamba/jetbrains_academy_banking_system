A = int(input())  # Sleep at least A hours a day
B = int(input())  # Sleep no more than B hours a day
H = int(input())  # Ann sleeps H hours a day

if H < A:
    print("Deficiency")
if A <= H <= B:
    print("Normal")
if B < H:
    print("Excess")
