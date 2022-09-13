import random                      #importing required modules
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

#game start
print(logo)
name = input("Welcome player, enter your character name: ")
print(f"Hi {name} you will have to guess the correct letters in the word to save the man from being hanged. You have 6 lives before the man hangs. All the best! \n")

#selecting random word from a list in another file within same directory


chosen_word = random.choice(word_list)
#print(chosen_word)                        #testing

word_length = len(chosen_word)            #length of chosen word

word_play = list()                       #empty list to create display

for letter in range(0,word_length):      #creating blank display
    word_play.append("_") 
print(f"\nThe word has {word_length} letters. Good luck!\n")


# loop until no blank remains
game_end = False
lives = 6
while not game_end:
    
    #getting user input
    guess = input("\nGuess a letter: ").lower()

    clear()

    if guess in word_play:
        print("\nYou have already guessed this letter. Select another\n")

    #checking if user input is in the word and replacing blank with guess

    for letter in range(word_length):
        
        if chosen_word[letter]== guess:
            print("\nYou have guessed correct!")            
            word_play[letter] = guess

    
                   
    print(f"{' '.join(word_play)}") #convert list to string
    
       #reducing player lives 
    if guess not in chosen_word:
        lives -=1
        print("\nWrong guess, you loose one life!")
    print(stages[lives])
             
 #win and lose conditions
    
    if not "_" in word_play :
        game_end = True
        print("Congrats, you have saved the man from being hanged. You win!")

    elif lives == 0:
        game_end = True
        print(f"The correct word was {chosen_word}. \n")
        print("The man is hanged. You lost!")