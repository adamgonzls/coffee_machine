from data import MENU, resources
print(MENU)

money = 0


def show_resources():
    for resource in resources:
        if resource == 'water' or resource == 'milk':
            print(f"{resource.capitalize()}:{resources[resource]}ml")
        elif resource == 'coffee':
            print(f"{resource.capitalize()}:{resources[resource]}g")
    print(f"Money: ${money}")


def start_process():
    user_selection = input(f"what would you like? (espresso/latte/cappuccino): ")

    print(f'You selected: {user_selection}')

    if user_selection == 'report':
        show_resources()
    elif user_selection == 'espresso' or user_selection == 'latte' or user_selection == 'cappuccino'



    #TODO: 1. Print report of all coffee resources


    start_process()


start_process()

# coin operated - penny, dime, nickel, quarter
# program requirements:
# 1. print report (how many resources are left remaining),
# 2. check resources are sufficient
# 3. process coins
# 4. check transaction successful.
# 5. Make coffee (deduct resources)

# What would you like? (espresso/latte/cappuccino): report
# Water: 300ml
# Milk: ...