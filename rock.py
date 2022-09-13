import random

#score counter
user_score = 0
comp_score = 0
draw_score = 0
options = ["rock", "paper", "scissors"]
while True:
    #check if user wants to quit
    user_input = input("Select your hand: Rock/paper/scissors or q to quit: ").lower()
    if user_input == "q":
        break
    #check if user entered valid option
    if user_input not in options:
        print("Not a valid option")
        continue
    #generate random number to assign computer options: rock - 0, paper -1, scissors -2
    random_number = random.randint(0,2)
    comp_hand = options[random_number]
    print("Computer picked: ",comp_hand)

    #gameplay logic
    if user_input == "rock" and comp_hand == "scissors":
        print("You win!")
        user_score += 1

    elif user_input == "paper" and comp_hand == "rock":
        print("You win!")
        user_score += 1

    elif user_input == "scissors" and comp_hand == "paper":
        print("You win!")
        user_score += 1
    elif user_input == comp_hand:
        draw_score += 1
        print("Draw, play again")
    else:
        print("Computer wins")
        comp_score += 1

print("Your score is: ", user_score)
print("Computer score is: ", comp_score)
print(f"You drawed {draw_score} times.")
print("Thanks for playing. Goodbye!")