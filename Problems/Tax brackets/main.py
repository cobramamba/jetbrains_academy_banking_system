income = int(input())
percent = int(0)
calculated_tax = int(0)

if 0 <= income <= 15527:
    percent = 0
elif 15528 <= income <= 42707:
    percent = 15
elif 42708 <= income <= 132406:
    percent = 25
else:
    percent = 28

calculated_tax = round(income * percent / 100)

print("The tax for " + str(income) + " is " + str(percent) + "%. That is " + str(calculated_tax) + " dollars!")
