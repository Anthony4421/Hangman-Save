#Hangman Game
#Anthony Swift
#29/06/2020

import random

#Asks the player if they would like to load the game saved
#If the player selects they would like to load the saved game
#Stores the relevant game data from the save text file based on which line number the data is on
#Lets the player know if there is no game saved and continues the game

def load_game(word, correct_guessed, letters_used, guesses):
    
    load = input("Would you like to load a saved game? (Y/N): ").upper()
    
    while load != "Y" and load != "N":
        load = input("Would you like to load the saved game? (Y/N): ").upper()
     
    if load == "Y":
 
        line_number = 0
        try:
            file = open("save.txt", "r")
            for line in file:
                line = line.strip()
                line_number += 1
                if line_number == 2:
                    guesses = line
                if line_number == 4 and line != "":
                    correct_guessed = line.split(',')
                if line_number == 6 and line != "":
                    letters_used = line.split(',')
                if line_number == 8:
                    word = line

            guesses = int(guesses)
        except IOError:
            print("No games to load")
            load = "N"


   
    return(word, load, correct_guessed, letters_used, guesses)

#Picks a random word for list words in txt file

def pick_word():

    #Stores the words from the words file

    all_words = []

    #Open words file
    #Loops through each line
    #Appends each word to the all_words list

    file = open("words.txt", "r")

    for line in file:
        line = line.strip()
        all_words.append(line)

    file.close()

    #Picks a random word from the all_words list
    #for the player to guess
    #and stores in the word variable
    #Ensures the word picked is between 5 and 12 characters
    word = random.choice(all_words)
    while len(word) < 5 or len(word) > 12:
        word = random.choice(all_words)
    print("\n")
    print(word)
    
    return word

#Welcome player

def welcome():

    print("\nWelcome to Hangman!\n")

#Ask player to guess letter

def guess_letter():

    letter = input("\nGuess your letter: ").upper()
    return(letter)

#Checks to see if the letter player guessed is in the word
#Displays whether the letter is correct or incorrect player
#If the letter has already been guessed by the player
#Lets the player know the letter has been used

#Input validation to check a valid letter has been guessed

def check_letter(word, letter, correct_guessed, letters_used, guesses):

    if len(letter) != 1 or letter.isalpha() == False:
        print("\nNot a valid letter")
    elif letter not in letters_used:
        if letter in word:
            print("\nCorrect!")
            correct_guessed.append(letter)
            letters_used.append(letter)
        else:
            print("\nIncorrect!")
            letters_used.append(letter)
            guesses -= 1
            
    else:
        print("\nLetter already guessed!")
    return guesses

#Displays letters to the user during each guess
#Displays letters guessed in the correct position
#Displays '-' when letter has not been guessed in position

def display_letters(correct_guessed, word):

    letters = ""
    for x in range(0, len(word)):
        if word[x] in correct_guessed:
            letters += word[x]
        else:
            letters += "-"
    print("\n")
    print(letters)
    return letters

#Ask the player if they would like to save the game at start of every turn
#Saves the relevant game information into a text file

def save_game(guesses, correct_guessed, letters_used, word):

    save = input("Would you like to save the game? (Y/N): ").upper()
    while save != "Y" and save != "N":
        save = input("Would you like to save the game? (Y/N): ").upper()

    if save == "Y":    

        #Convert correct_guessed and letters_used variables to string

        correct_guessed = ','.join(correct_guessed)
        letters_used = ','.join(letters_used)
    
        file = open("save.txt","w")

        file.write("Guesses: ")
        file.write("\n")
        file.write(str(guesses))
        file.write("\n")
        file.write("Correct Guessed: ")
        file.write("\n")
        file.write(correct_guessed)
        file.write("\n")
        file.write("Letters Used: ")
        file.write("\n")
        file.write(letters_used)
        file.write("\n")
        file.write("word: ")
        file.write("\n")
        file.write(word)
    
#Displays if the player has won or lost

def display_result(guesses, word):

    if guesses == 0:
        print("\nYou have lost! ")
    else:
        print("\nCongratulations! You have won")

#At the end of the game asks player if they want to play again

def play_again():

    gameplay = input("\nWould you like to play again? (Y/N):").upper()
    while gameplay != "Y" and gameplay != "N":
        gameplay = input("Would you like to play again? (Y/N):").upper()
        
    return gameplay

#Displays the appropriate scaffold to the player
#Depending on how many guesses the player has left

def display_scaffold(guesses):

    if guesses == 6:
        print("""

          ----------
          |/       |
          |     
          |       
          |       
          |
         ---

         """)

    elif guesses == 5:
        print("""

          ----------
          |/       |
          |        0
          |       
          |       
          |
         ---

         """)
        
    elif guesses == 4:
        print("""

          ----------
          |/       |
          |        0
          |        |
          |       
          |
         ---

         """)
        
    elif guesses == 3:
        print("""

          ----------
          |/       |
          |        0
          |       /|
          |       
          |
         ---

         """)

    elif guesses == 2:
        print("""

          ----------
          |/       |
          |        0
          |       /|/
          |       
          |
         ---

         """)

    elif guesses == 1:
        print("""

          ----------
          |/       |
          |        0
          |       /|/
          |       /
          |
         ---

         """)

    elif guesses == 0:
        print("""

          ----------
          |/       |
          |        0
          |       /|/
          |       / /
          |
         ---

         """)

#The Main Function
        
def main():
    gameplay = "Y"
    while gameplay == "Y":
        guesses = 6
        letters_used = []
        correct_guessed = []
        word = ""
        welcome()
        word, load, correct_guessed, letters_used, guesses = load_game(word, correct_guessed, letters_used, guesses)
        if load == "N":
            word = pick_word()
        letters = display_letters(correct_guessed, word)
        display_scaffold(guesses)
        while letters != word and (guesses > 0):
            save_game(guesses, correct_guessed, letters_used, word)
            letter = guess_letter()  
            guesses = check_letter(word, letter, correct_guessed, letters_used, guesses)
            letters = display_letters(correct_guessed, word)
            display_scaffold(guesses)
        display_result(guesses, word)
        gameplay = play_again()

main()










    
    
