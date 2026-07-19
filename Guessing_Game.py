import random 

jackpot = random.randint(1, 100)
guess=int(input("Guess a number between 1 and 100: "))
count=1
while guess != jackpot:
    if guess<jackpot:
        print("Too low! guess higher.")
    else:
        print("Too high! guess lower.")
    guess=int(input("Guess again: "))
    count+=1
    
print("Congratulations! You guessed the correct number:", jackpot)
print("It took you", count, "guesses to find the correct number.")