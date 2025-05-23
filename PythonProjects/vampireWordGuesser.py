import random

# words that user has to guess
word_bank = ['twilight', 'vampires', 'lestat', 'akasha', 'claudia', 'garlic', 'nosferatu',
             'dracula', 'orleans', 'nadja', 'nandor', 'lazlo', 'armand', 'stake', 'cullen', 'edward']

# randomly select the word
word = random.choice(word_bank)

# create a word blank
guessedWord = ['_'] * len(word)

# how many tries the user has to guess
attempts = 10

# while there are still attempts
while attempts > 0:

    # print out the letters available
    print('\nCurrent Word: ' + ' '.join(guessedWord))

    guess = input('Guess a letter: ')

    # replace the blank spot in the letter
    if guess in word: 
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great guess!')
    # subtract an attempt
    else: 
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
    # once user finishes guessing the word
    if '_' not in guessedWord:
        print('\nCongratulations! You guessed the word: ' + word)
        break
    
if '_' in guessedWord:
     print('\nYou\'ve run out of attempts! The word was: ' + word)
        
