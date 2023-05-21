import random
n = random.randrange(1,10)
guess = int(input("Enter a number between 1 to 10"))
while n!=value:
    if guess > n:
        print("Bhai bhut badha soch liya thoda kam")
        guess = int(input("Enter again"))
    elif guess < n:
        print("Bhai bhut kam h value thoda jayada soch")
        guess = int(input("Enter again"))
    else:
        break

print("You Guessed Right")
print("Congrates")
