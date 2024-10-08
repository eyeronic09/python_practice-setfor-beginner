
import random

n = random.randint(1, 9) 
a = -1


while a != n:
    try:
        a = int(input("Guess the number: "))
        if a > n:
            print("Lower number please")
        elif a < n:
            print("Higher number please")
    except ValueError:
        print("Please enter a valid integer.")

print(f"You have guessed the number {n}")
