import random
from words import words
from Hangman_vis import lives_visual_dict
import string

def getValidWords(words):
    word = random.choice(words)
    while "-" in word or "" in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = getValidWords(words)
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()

    lives = 7

    while len(wordLetters) > 0 and lives > 0:
        print(f"You have {lives} left and you have used these letters: ", "".join(usedLetters))
        
        wordList = [letter if letter in usedLetters else "-" for letter in word]
        print(lives_visual_dict[lives])
        print("Current word: ", "".join(wordList))

        userLetter = input("Guess a letter: ").upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
                print("")

            else:
                lives = lives - 1
                print(f"Your letter, {userLetter} is not in the word.")

        elif userLetter in usedLetters:
            print(f"You have already guessed that letter. Guess another.")
        else:
            print("That is not a valid letter.")

    if lives == 0:
        print(lives_visual_dict[lives])
        print(f"You've lost! The word was {word}")
    else:
        print("Congratulations! You've won!")