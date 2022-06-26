import random
from datetime import datetime

guess = None
guessesTaken = 0
guesses = 5
number = random.randint(1, 20)
print("Try to guess number from 1 to 20")

keyword = 'results'

while guessesTaken < guesses:
    raw_guess = input()
    guess = None

    if raw_guess == keyword:
        with open('results.txt', 'r') as f:
            lines = f.readlines()
            for _ in lines:
                print(_)

    elif raw_guess.isdigit():

        guess = int(raw_guess)

        guessesTaken += 1

        if guess < number:
            print("The number is bigger")
        elif guess > number:
            print("The number is lower")
        elif guess is number:
            print('Whoooaaa, you lucky dog, dude. You hit the number in ' + str(guessesTaken) + ' tries')
            with open('results.txt', 'a') as f:
                f.write('Game: ' + str(datetime.now()) + '\n')
                f.write('The number was: ' + str(number) + '\nNumber of guesses: ' + str(guessesTaken) + '\n')

            break
    elif raw_guess.isalpha():
        print("Your guess should be a number")
        continue

if guess != number:
    print("Whooaaa, you looser, my friend")
