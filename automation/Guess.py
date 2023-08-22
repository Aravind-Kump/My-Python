import random

print('Hello, what is your name ? ')
name = input()

secretNumber = random.randint(1, 20)
print('Hey ' + name + ' I am thinking of a number between 1 to 20, can you guess ?')

for guessNumber in range(1, 6):
    print('Take a guess:')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess value is too low')
    elif guess > secretNumber:
        print('Your guess value is high')
    else:
        break

if guess == secretNumber:
    print(
         'Good job !' + name    )
else:
    print('All attempts completed and you were wrong. The correct number is ' + str(secretNumber))