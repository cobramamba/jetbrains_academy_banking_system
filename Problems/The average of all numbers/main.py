a = int(input())  # put your python code here
b = int(input())
sum_numbers = int(0)

numbers = []

for index in range(a, b + 1):
    if index % 3 == 0:
        numbers.append(index)
        sum_numbers += index

print(float(sum_numbers / len(numbers)))
