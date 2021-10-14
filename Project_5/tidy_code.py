from random import randint as a

__author__ = ''
__email__ = '@nmbu.no'


# makes us guess a number until we guess 1 or more. Does not handle exceptions
def getUserInput():
    c = 0
    while c < 1:
        c = int(input('Your guess: '))
    return c


# returns a random number between 2 and 12
def getRandomNumber():
    return a(1, 6) + a(1, 6)


# returns true or false based on if f and g are equal or not
def checkIfEqual(f, g):
    return f == g


if __name__ == '__main__':

    correct_guess = False                                   # for ever loop
    counter = 3                                             # we have 3 guesses
    random_number = getRandomNumber()                       # finds the random number we have to guess
    while not correct_guess and counter > 0:
        user_input = getUserInput()                         # gets the user input
        correct_guess = checkIfEqual(random_number, user_input)             # checks if guess is correct
        if not correct_guess:
            print('Wrong, try again!')
            counter -= 1                                                    # goes down 1 for every guess, will exit on 0

    if counter > 0:
        print('You won {} points.'.format(counter))
    else:
        print('You lost. Correct answer: {}.'.format(random_number))
