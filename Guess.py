import random
def guess(x):
    random_number = random.randint(1,x)
    guess2 = 0
    while guess2 != random_number:
        guess2 = int(input(f'Guess a number between 1 and {x} '))
        if guess2 < random_number:
            print('Sorry, guess again. Too low.')
        elif guess2 > random_number:
            print('Sorry, guess again. Too high.')

    print('Yay, congrats. You have guessed the number',random_number,'correctly!')


guess(10)
