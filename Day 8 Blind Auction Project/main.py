from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to Blind Auction")
bidders_list = {}

flag = True
#Game Loop
while(flag):
  name = input("Enter your name :")
  bidders_list[name] = int(input("Enter your Bid : $"))
  response = input("Type Yes if there are any other bidders else type No :").lower()
  if(response == "no"):
    flag = False
  clear()


def highest_bidder(bidders_list):
  max_bidder = "Noone"
  max_amount = 0
  for bidder in bidders_list:
    if(bidders_list[bidder] > max_amount):
      max_bidder = bidder
      max_amount = bidders_list[bidder]

  print(f"The winner is {max_bidder} with a maximum bid of ${max_amount}")    

highest_bidder(bidders_list)  

