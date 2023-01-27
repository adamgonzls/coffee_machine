from data import MENU, resources
# print(MENU)

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
    quarters_amount = int(input("How many quarters?: "))
    dimes_amount = int(input("How many dimes?: "))
    nickels_amount = int(input("How many nickels?: "))
    pennies_amount = int(input("How many pennies?: "))


is_on = True
while is_on:
    user_selection = input(f"what would you like? (espresso/latte/cappuccino): ")

    print(f'You selected: {user_selection}')

    if user_selection == 'report':
        show_resources()
    elif user_selection in MENU:
        selected_drink_ingredients = MENU[user_selection]['ingredients']
        print("You chose a drink.")
        if check_drink_resources(selected_drink_ingredients):
            tender_payment()
    elif user_selection == 'off':
        is_on = False
    else:
        print("Please choose a valid selection.")

# coin operated - penny, dime, nickel, quarter
# program requirements:
# 1. print report (how many resources are left remaining),
# 2. check resources are sufficient
# 3. process coins
# 4. check transaction successful.
# 5. Make coffee (deduct resources)