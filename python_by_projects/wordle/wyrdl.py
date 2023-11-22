import pathlib
import random

WORDLIST = pathlib.Path('wordlist.txt')
words = [word.upper() for word in WORDLIST.read_text('utf-8').strip().split('\n')]
word = random.choice(words)
# WORD = 'SNAKE'
for guess_num in range(1,7):
    guess = input(f'\nGuess {guess_num}: ').upper()
    if guess == word:
        print('Correct')
        break
    else:
        print('Wrong')

    correct_letters = {letter for letter, correct in zip(guess, word) if correct == letter}
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)
    
    print('Correct letters: ', ', '.join(sorted(correct_letters)))
    print('Misplaced letters: ', ', '.join(sorted(misplaced_letters)))
    print('Wrong letters: ', ', '.join(sorted(wrong_letters)))