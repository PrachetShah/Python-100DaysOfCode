from game_data import data
import random
from art import logo, vs, thanks
from replit import clear

def random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(response, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return response == "a"
  else:
    return response == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = random_account()
  account_b = random_account()

  while game_should_continue:
    account_a = account_b
    account_b = random_account()

    while account_a == account_b:
      account_b = random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.\n")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}\n")
      print(thanks)

game()



