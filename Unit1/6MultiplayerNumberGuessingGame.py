#Single Player Guessing Game
#This game allows a player to guess a computer generated number


#VARIABLES
user_guess = -1
answer = -1
lives = 10


#BEGINNING OF GAME
print("Welcome to the Single Player Guessing Game")
print("Enter a number between 1-100 for the second player to guess")
answer = int(input("->"))
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

while(lives > 0):
    try:
        print("Guess a number between 1-100 chosen by the first user")
        user_guess=int(input("->"))
        print("You have guessed: ", user_guess)
        print("You have ", lives, "lives left.")
        if user_guess == answer:
            print("You Win!")
            break
        elif user_guess > answer:
            print("Guess Lower")
            lives = lives - 1
        elif user_guess < answer:
            print("Guess Higher")
            lives = lives - 1
        else:
            print("Error")
    except:
        print("An error has occurred, please try again")
print("Thanks for playing!")
print("The secret number was", answer)

