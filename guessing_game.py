"""A guessing game"""
from random import randint

def main():
    """the main routine"""

    guesses_taken = 0
    my_name = raw_input('Hello! What is your name?\n')

    number = randint(1, 20)
    print'Well, {0}, I am thinking of a number '\
            'between 1 and 20'.format(my_name)

    while guesses_taken < 6:
        guess = int(raw_input('Take a guess.\n'))
        guesses_taken += 1

        if guess < number:
            print 'Your guess is too low.'
        elif guess > number:
            print 'Your guess is too high.'
        else:
            break

    if guess == number:
        print 'Good job, {0}! You guessed my '\
                'number in {1} guesses!'.format(my_name, guesses_taken)
    else:
        print 'Nope. The number I was thinking of was {0}'.format(number)

if __name__ == "__main__":
    main()
