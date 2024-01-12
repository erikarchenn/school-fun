
# Name: Erika Chen
# Collaborators: N/A

import random
import string

# -----------------------------------
# HELPER FUNCTIONS
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER FUNCTIONS
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in secret_word:
        if i not in letters_guessed:
            return False
    
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    this_str = ""
    for i in secret_word:
        if i in letters_guessed:
            this_str += i
        else:
            this_str += "*"
    return this_str


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_str = "abcdefghijklmnopqrstuvwxyz"
    letters = ""
    for i in my_str:
        if i not in letters_guessed:
             letters += i
    return letters

def revealed__random_letter(secret_word, letters_remaining):
    revealed_letter = ''
    for i in secret_word:
        if i in letters_remaining:
            revealed_letter += i
    new = random.randint(0, len(revealed_letter)-1) #random integer from range btwn 0 and length of revealed letter
    revealed_letter = revealed_letter[new]
    return revealed_letter

def unique_chars(secret_word):
    new_letters = '' 
    for i in secret_word:
        if i in new_letters:
            continue
        new_letters += i
    return new_letters


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '$'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol $, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    vowels = "aeiou"
    guesses_remaining = 10
    print("Welcome to hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("------------")
    while True:
        print ("You have " + str(guesses_remaining) + " guesses left.")
        print ("Letters: " + get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ")
        if guess == '$' and with_help:
            if guesses_remaining < 3:
                print("Oops! Not enough guesses left: " , get_word_progress(secret_word, letters_guessed))
            else:
                revealed_letter = (revealed__random_letter(secret_word , get_available_letters(letters_guessed)))
                letters_guessed.append(revealed_letter)
                print ("Letter revealed: " , revealed_letter)
                print(get_word_progress(secret_word, letters_guessed))
                guesses_remaining -=3
        elif guess in secret_word and guess not in letters_guessed:
            letters_guessed.append(guess)
            print("Good guess: " , get_word_progress(secret_word, letters_guessed))
        elif guess in letters_guessed:
            print("Oops! You've already guessed that letter: " + get_word_progress(secret_word, letters_guessed))
        else:
            letters_guessed.append(guess)
            print("Oops! That letter is not in my word: " + get_word_progress(secret_word, letters_guessed))
            if guess not in vowels:
                guesses_remaining -= 1
            else:
                guesses_remaining -= 2
        print("----------")
        if guesses_remaining == 3:
            print("Warning: you have three guesses remaining.")
        if guesses_remaining <= 0:
            print("You're out of guesses. The word was " + secret_word + ".")
            break

        if has_player_won(secret_word, letters_guessed):
            print ("Congratulations! You won!")
            total_score = (guesses_remaining + (2 * len(unique_chars(secret_word))) + (3 * len(secret_word)))
            print ("Your total score for this game is: " , total_score)

            break
     
     

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    secret_word = "supercalifragilisticexpialidocious"
    with_help = True
    hangman(secret_word, with_help)
    # To test your game, uncomment the following three lines.

    # secret_word = choose_word(wordlist)
    # with_help = False
    # hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "$" as a guess!

    ###############

