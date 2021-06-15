import random

words = ['STUNTMAN', 'ORANGE', 'MIRROR', 'CAR', 'BANANA', 'COMPUTER', 'MONSTER', 'BRIDGE', 'ROCKET', 'EMERGENCY', 'RABBIT', 'TRUCK', 'AIRPLANE', 'FOREST', 'MACHINEGUN', 'PENGUIN', 'FARMER', 'FISH', 'YARN', 'EXCELENT']

guesses = ''

turns = 10

secret_word = words[random.randint(0,len(words)-1)]

while turns > 0:

    guess = input("\nGuess a character/word:")

    if guess.upper() in guesses:
        print('You already guessed', guess.upper())
    elif guess.upper() not in secret_word:
        guesses += guess.upper()
        turns -= 1
        for char in secret_word:
            if char in guesses:
                print(char.upper() + ' ', end='')
            else:
                print('_ ', end='')
    else:
        guesses += guess.upper()
        for char in secret_word:
            if char in guesses:
                print(char.upper() + ' ', end='')
            else:
                print('_ ', end='')

    if guess.upper() == secret_word:
        print('\nYou win!')
        secret_word = words[random.randint(0,len(words)-1)]
        turns = 10
        guesses = ''
    elif turns == 0:
        print('\nYou got hanged!')
        print('The word was', secret_word.upper())
        break
    else:
        print('\nYou got', turns, 'turns left')