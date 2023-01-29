from data import MENU, resources

revenue = 0


def show_resources():
    """Prints report of resources"""
    for resource in resources:
        if resource == 'water' or resource == 'milk':
            print(f"{resource.capitalize()}: {resources[resource]}ml")
        elif resource == 'coffee':
            print(f"{resource.capitalize()}: {resources[resource]}g")
    print(f"Revenue: ${revenue}")


def check_drink_resources(selected_drink_ingredients):
    """checks if enough resources are available to make drink"""
    print(f'{selected_drink_ingredients}')
    for ingredient in selected_drink_ingredients:
        if resources[ingredient] < selected_drink_ingredients[ingredient]:
            print(f'Sorry, there is not enough {ingredient}')
            return False
    return True


def tender_payment():
    print('Please insert coins.')
    total_tendered = 0
    quarters_amount = int(input("How many quarters?: "))
    dimes_amount = int(input("How many dimes?: "))
    nickels_amount = int(input("How many nickels?: "))
    pennies_amount = int(input("How many pennies?: "))

    total_tendered += quarters_amount * .25
    total_tendered += dimes_amount * .10
    total_tendered += nickels_amount * .05
    total_tendered += pennies_amount * .01
    return total_tendered


def dispense_drink(selected_drink_ingredients):
    for ingredient in selected_drink_ingredients:
        resources[ingredient] -= selected_drink_ingredients[ingredient]


def dispense_change(money_deposited, selected_drink_cost):
    print(f"Amount deposited: {money_deposited} Drink cost: {selected_drink_cost}")
    global revenue
    revenue += selected_drink_cost
    return round(money_deposited - selected_drink_cost, 2)


is_on = True
while is_on:
    user_selection = input(f"what would you like? (espresso/latte/cappuccino): ")

    print(f'You selected: {user_selection}')

    if user_selection == 'report':
        show_resources()
    elif user_selection in MENU:
        selected_drink_ingredients = MENU[user_selection]['ingredients']
        if check_drink_resources(selected_drink_ingredients):
            selected_drink_cost = MENU[user_selection]['cost']
            money_deposited = tender_payment()
            if money_deposited >= selected_drink_cost:
                dispense_drink(selected_drink_ingredients)
                users_change = dispense_change(money_deposited, selected_drink_cost)
                print(f"Here is {users_change} in change. Here is your {user_selection}. Enjoy!")
            else:
                print('Sorry that is not enough money. Money refunded.')
    elif user_selection == 'off':
        print("Powering off machine.")
        is_on = False
    else:
        print("Please choose a valid selection.")