#Link to Tip Calculator Project :

#https://replit.com/@PrachetShah/tip-calculator?embed=1&output=1#main.py

#Code:
print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill :$"))
tip_percent = int(input("What percentage tip would you like to give 10,12, or 15 :"))
total_bill = bill + bill*tip_percent/100
people = int(input("How many people to split the bill? "))
bill_of_person = round(total_bill/people, 2)
print("Each person should pay ${:.2f}".format(bill_of_person))
