import random


def guess(x):
    attempts = 0
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x} :"))
        attempts += 1
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
        print("This is your ", attempts, " attempt!")

    print("Yay, congrats. You have guessed the number", random_number, "correctly!")
    print("------------o------------")
    print("You did it in: ", attempts, "attempts!")


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    attempts = 0
    while feedback != "c":

        attempts += 1
        print("This is my ", attempts, " attempt!")
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is {guess}: too high (h), too low (L), or correct (C)?? ")
        if feedback == "h":
            high = guess - 1

        elif feedback == "l":
            low = guess + 1

    print(f"Yay! the computer guessed your number", guess, "correcly")
    print("------------o------------")
    print("It did it in: ", attempts, "attempts!")


guess(10)
computer_guess(10)
