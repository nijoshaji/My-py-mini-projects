name = input("Set character name: ")  # setting character name
print('Welcome', name, 'to this simple quiz')
play = input('Would you like to play? yes or no ').lower()
if play != "yes":
    print('Goodbye')
    quit()
else:
    print("Let's begin")

score = 0  # scoreboard

# question blocks

q1 = input("What is the capital of India? ").lower()
if q1 == "new delhi":
    print("Correct")
    score += 1
else:
    print("Incorrect")

q1 = input("What is the capital of United Kingdom? ").lower()
if q1 == "london":
    print("Correct")
    score += 1
else:
    print("Incorrect")

q1 = input("What is the capital of Canada? ").lower()
if q1 == "toronto":
    print("Correct")
    score += 1
else:
    print("Incorrect")

q1 = input("What is the capital of Australia? ").lower()
if q1 == "sydney":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("Your score is", score)
