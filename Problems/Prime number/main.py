num = int(input())

# prime numbers are > 1
if num > 1:
    for index in range(2, num):
        if (num % index) == 0:
            print("This number is not prime")
            # print(index, "times", num // index, "is", num)
            break
    else:
        print("This number is prime")
# non prime numbers are <= 1
else:
    print("This number is not prime")
