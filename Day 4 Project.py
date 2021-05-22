#Link to Project:

#https://replit.com/@PrachetShah/rock-paper-scissors?embed=1&output=1#main.py

#Code:
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
choice = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors. :"))
image_choice = [rock,paper,scissors]
print(image_choice[choice])
   

comp_choice = random.randint(0,2)
print("Computer Chooses:\n"+image_choice[comp_choice])

#To predict result
if(choice == comp_choice):
  print("It's a Draw")
elif(choice == 0 and comp_choice == 1):
  print("You Lose")  
elif(choice == 0 and comp_choice == 2):
  print("You Win")
elif(choice == 1 and comp_choice == 0):
  print("You Win")  
elif(choice == 1 and comp_choice == 2):
  print("You Lose") 
elif(choice == 2 and comp_choice == 0):
  print("You Lose") 
elif(choice == 2 and comp_choice == 1):
  print("You Win")                
