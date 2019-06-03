# Import a library
import random

print('---------------------------------')
print('          GUESS A NUMBER         ')
print('---------------------------------')
print()

guess = -1
number = random.randint(0, 100)
name = input('What is your name?')

while guess != number:
    guess = int(input('Guess a number between 0 and 100: '))

    if guess < the_number:
        print('Sorry {}, your guess of {} was too LOW.'.format(name, guess))
    elif guess > the_number:
        print('Sorry {}, your guess of {} was too HIGH.'.format(name, guess))
    else:
        print('Excellent work {}, you won, it was {}!'.format(name, guess))

print('done')
