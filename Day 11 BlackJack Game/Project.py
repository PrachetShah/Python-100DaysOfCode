import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(a_list):
    """Take a list of cards and return the sum of those cards"""
    if sum(a_list) == 21 and len(a_list) == 2:
        # print("Blackjack")
        return 0 #0 represents blackjack in our game
    if 11 in a_list and sum(a_list) > 21:
        a_list.remove(11)
        a_list.append(1)
    return sum(a_list)

user_win = 0
comp_win = 0

def compare(user_score,computer_score):
    global user_win
    global comp_win
    if user_score == computer_score:
        user_win += 1
        return "\nDraw 🙃"
    elif computer_score == 0:
        comp_win += 1
        return "\nLose, opponent has BlackJack 😱"
    elif user_score == 0:
        user_win += 1
        return "\nWin with a BlackJack 😎"
    elif user_score > 21:
        comp_win += 1
        return "\nYou went over. You Lose 😭"
    elif computer_score > 21:
        user_win += 1
        return "\nOpponent Went Over, You Win 😁"
    elif user_score > computer_score :
        user_win += 1
        return "\nYou Win, your score is higher 😌"
    else:
        comp_win += 1
        return "\nYou Lose, your score is lower than  computer's ☹️"

def play_game():
    user_cards, computer_cards = [], []
    is_game_over = False
    #add 2 random cards to user and computers hand
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"User Cards: {user_cards} and Current Score : {user_score}")
        print(f" Computer Card : {computer_cards[0]} ")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card , type'n' to pass :")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while(computer_score !=0 and computer_score < 17):
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"\n  Your final hand : {user_cards}, final score : {user_score}")
    print(f"  Computer final hand : {computer_cards}, final score : {computer_score}")
    print(compare(user_score,computer_score))

print(logo)
while input("\nDo you want to play a  game of BlackJack? Type 'y' or 'n' :") == 'y':
    play_game()
print(f"       You have won {user_win} times and computer has won {comp_win} times       ")
from art import thanks
print(thanks)

