import random

print('Hello !, what is your name ??')
name = input()

print('Hey, ' + name + '!!! I am thinking of a number between 1 and 20 ')
secretNumber = random.randint(1, 20)

print('DEBUG: Secret number is ' + str(secretNumber))

for guessesTaken in range(1, 6):
    print("Take a Guess")
    guess=int(input())

    if guess < secretNumber:
        print( name + '! your guess is too low')
    elif guess > secretNumber:
        print( name + '! your guess is too high')
    else:
        break
if guess == secretNumber:
    print('Good Job' + name + '! You guessed it right')
else:
    print('Nope, the number i was thinking of was ' + str(secretNumber))