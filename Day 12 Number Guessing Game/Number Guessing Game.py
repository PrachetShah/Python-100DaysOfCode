from art import logo
print(logo)
import random

print("Welcome to Number Guessing Game")
print("I am choosing a number from 1 to 100")
num_choice = random.choice(range(1,101))

response = input("Enter which level : 'easy' or 'hard' :")

def easy():
    is_game_over = False
    attempts = 10
    print(f"You have {attempts} to clear this stage")
    num_choice = random.choice(range(1, 101))
    while not is_game_over:
        if attempts == 0:
            is_game_over = True
            print("Game Over , You Lose")
        num = int(input("\nGuess a Number :"))

        if(num > num_choice):
            attempts -=  1
            print("Too High, Guess Lower")
            print(f"You have {attempts} attempts left")
        elif(num < num_choice):
            attempts -= 1
            print("Too Low, Guess Higher")
            print(f"You have {attempts} attempts left")
        elif(num == num_choice):
            print(f"Great Job, you guessed it correct ,the number was {num_choice}")
            is_game_over = True


def hard():
    is_game_over = False
    attempts = 5
    print(f"You have {attempts} attempts to clear this stage")
    num_choice = random.choice(range(1, 101))
    while not is_game_over:
        if attempts == 0:
            is_game_over = True
            print("Game Over , You Lose")
        num = int(input("\nGuess a Number :"))
        if (num > num_choice):
            attempts -= 1
            print("Too High, Guess Lower")
            print(f"You have {attempts} attempts left")
        elif (num < num_choice):
            attempts -= 1
            print("Too Low, Guess Higher")
            print(f"You have {attempts} attempts left")
        elif (num == num_choice):
            print(f"Great Job, you guessed it correct ,the number was {num_choice}")
            is_game_over = True

if response == 'easy':
    easy()
elif response == 'hard':
    hard()
else:
    print("Enter Valid Option")







