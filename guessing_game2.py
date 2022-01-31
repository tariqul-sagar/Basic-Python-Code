print('\n       A digit place Guessing game')
import random
m = int(input("Enter a 4 digit number: "))
nump = random.randint(1000,9999)
while m!= 10:
    num = nump
    correct = 0
    while num%10000:
        numc = num%10
        nc = m%10
        num = num//10
        m=m//10
        if numc == nc:
            correct+=1
    if correct == 4:
        print("Congrats! You guessed it right.")
        break
    else:
        print("%d digits were guessed right." %correct)
        m = int(input("Enter a 4 digit number: "))
else:
    print("You quit the game.")