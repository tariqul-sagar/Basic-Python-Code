import random
n = random.randint(1,20)
g_count = 0
g_limit = 2
num = int(input("Guess an integer between 1 to 20: "))
while g_count < g_limit:
    number = int(input("Sorry! Guess again: "))
    g_count +=1
    if number == n:
        print("You Won!")
        print(f"The guess number is {n}")
        break
else:
    print("You failed! Better Luck Next Time.")
    print(f"The number is {n}")

