import random


def guess_number():
    a = random.randint(0, 100)
    print(a)
    while True:
        b = int(input("Enter a Number: "))
        if b == a:
            print("You guessed it!")
            break
        else:
            if b > a:
                print("Too high, Try again")
            else:
                print("too low, Try again")


guess_number()
