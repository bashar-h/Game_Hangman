import random
import string

from words import words
alphabet = set(string.ascii_uppercase)

def pick_word(x):
    word = random.choice(x).upper()
    while "-" in word or " " in word:
        word = random.choice(x).upper()
    return word

def play():
    
    word = pick_word(words)
    wordletters = set(word)
    guessed = []

    currentword = " ".join([letter if letter in guessed else "-" for letter in word])

    lives = 5
    print(f"Let's start the game! you have to guess the following word, and you have only {lives} lives!")
    print (currentword)

    while len(wordletters) > 0 and lives > 0 :
        guess = input ("\nGuess a letter : ").upper()
        if guess in wordletters:
            guessed.append(guess)
            wordletters.remove(guess)
            currentword = " ".join([letter if letter in guessed else "-" for letter in word])
            print("\nCorrect! you have guessed a correct letter!")
            print ("The word is:",currentword)
        elif guess in guessed:
            print("\nYou have alreay guessed this letter! Try a new one.")
        elif not(guess in alphabet):
            print("\nNot a valid letter, try again.")
        else:
            guessed.append(guess)
            lives = lives -1
            print(f"\nThat is a wrong letter! Try a new one... You have only {lives} left!")

    if lives == 0:
        print(f"Sorry you have lost :( The correct word is {word}")
    else:
        print("Congrats! You have won!")
    
play()

more=input("\nTo play again type \"Y\" then press Enter ").upper()
print (more)
while more == "Y":
    print("\n\n\n")
    play()
    more=input("\nTo play again type \"Y\" then press Enter ").upper()
    
