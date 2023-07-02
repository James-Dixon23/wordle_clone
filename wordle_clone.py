import typing
import random

with open('gamewords.txt', 'r') as file:
    # Create an empty list to store the words and append each word to the list
    game_words = []
    for line in file:
        line = line.strip()
        game_words.append(line)

#function to get a guess from the user and return a valid guess in all capitals. 
#If the guess is not the correct length or not a valid word, give an error message and ask for another guess.

def get_guess(word_len: int, word_list: typing.Set[str]):

    #Get a guess from the user and return a valid guess in all capitals.
    #else give error message

    while True:
        guess = input("Guess a word: ")
        if len(guess) != word_len:
            print(f"Your guess must be {word_len} letters long.")
        elif guess not in word_list:
            print("Your guess must be a valid word.")
        else:
            guess = guess.upper()
            return guess

def compare_word(expected: str, guess: str):

    #Compare the expected word with the guess and return the number of matching letters.
    #If the letter is in the correct place, add it to the in_place list.
    #If the letter is in the wrong place, add it to the out_of_place list and add a blank space to in_place list.
    #return both lists

    in_place = []
    out_of_place = []
    for i in range(len(expected)):
        if expected[i] == guess[i]:
            in_place.append(expected[i])
        elif (expected[i] in guess) and (expected[i] != guess[i]):
            out_of_place.append(expected[i])
            in_place.append("_")
        else:
            in_place.append("_")
    return in_place, out_of_place


#main function which runs the game by picking a random word from list and calling the get_guess and compare_word functions to allow the player to guess the word

if __name__ == '__main__':
    WORD = random.choice(game_words)
    WORD = WORD.upper()
    count =  0
    
#attempt to guess a word, if CTRL+C is pressed, exit the program
    
    try:
        while True:
            GUESS = get_guess(len(WORD), game_words)
            if WORD == GUESS:
                print("You win!")
                print(f"It took you {count} guesses.")
                break

#compare the guess with the word and print the number of letters in the correct place and the number of letters in the wrong place
            
            else:
                compare = compare_word(WORD, GUESS)
                print(f"Letters in the correct place: {compare[0]}")
                print(f"Letters in the wrong place: {compare[1]}")
                print("Try again!")
                count += 1
#exit the program if CTRL+C is pressed
   
    except KeyboardInterrupt:
        print("Bye!")