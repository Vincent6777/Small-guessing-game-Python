import random
x = random.randint(1, 100)
b = None
while b != x:
    b = int(input("Guess the number between 1 and 100"))
    if b != x:
        print("False, Try again")
    elif b == x:
        print("Congrats, you guessed the number")