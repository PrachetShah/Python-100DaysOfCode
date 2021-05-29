
#Importing Data
profit = 0
from Menu import resources,MENU

# TODO: 4 Check resources sufficient?
def check_resources(order):
    """Returns True when orden can be made, False if ingredients missing"""
    for item in order:
        if order[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

# TODO: 5 Process coins
def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    quarter = 0.25 * int(input("Enter Quarters : $"))
    dime = 0.1 * int(input("Enter Dimes : $"))
    nickel = 0.05 * int(input("Enter Nickels : $"))
    penny = 0.01 * int(input("Enter Pennies : $"))
    total_cash = quarter + dime + nickel + penny
    return total_cash

# TODO: 6 Check transaction successful?
def transaction_success(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is the ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry thats not enough. Money Refunded")
        return False

# TODO: 7 Make Coffee.
def make_coffee(drink_name, order):
    """remove the ingredients from resources to make coffee"""
    for item in order:
        resources[item] -= order[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


# TODO: 2 Turn off the Coffee Machine by entering “off” to the prompt
# TODO: 3 Print report.
shut_down = False
while not shut_down:
    response = input("What would you like? (espresso/latte/cappuccino): ")
    if response == 'off':
        print("Under Maintenance")
        shut_down = True
    elif response == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[response]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            if transaction_success(payment, drink["cost"]):
                make_coffee(response, drink['ingredients'])

