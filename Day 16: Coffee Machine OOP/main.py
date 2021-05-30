from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

shut_down = False

while not shut_down:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        shut_down = True
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        payment_successful = money_machine.make_payment(drink.cost)
        if enough_ingredients and payment_successful:
            coffee_maker.make_coffee(drink)
