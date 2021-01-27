year = int(input())  # put your python code here

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Leap')
else:
    print('Ordinary')
