from internal import resources, MENU


def report(coffee_type, _resources):
    _resources["water"] -= coffee_type["ingredients"]["water"]
    _resources["milk"] -= coffee_type["ingredients"]["milk"]
    _resources["coffee"] -= coffee_type["ingredients"]["coffee"]
    _resources["money"] += coffee_type["cost"]
    return _resources


def coin_processor(order):

    total = int(input("Quarters :")) * 0.25
    total += int(input("Dimes :")) * 0.10
    total += int(input("Nickles :")) * 0.05
    total += int(input("Pennies :")) * 0.01

    if total < MENU[order]["cost"] :
        print(f"You dont have enough Money, need more ${round(MENU[order]["cost"] - total, 2)}")

    else:
        print(f"Get your change :{round(total - MENU[order]["cost"], 2)}")
        report(MENU[order], resources)
        print(f"Enjoy your '{order}'")


def sufficient(order, _resources):
    if _resources["water"] < MENU[order]["ingredients"]["water"]:
        print("Insufficient 'Water'.")
        return False
    elif resources["milk"] < MENU[order]["ingredients"]["milk"]:
        print("Insufficient 'Milk'.")
        return False
    elif resources["coffee"] < MENU[order]["ingredients"]["coffee"]:
        print("Insufficient 'Coffee'.")
        return False
    else:
        return True


def after_sufficient(order):
    print("Enter Coins Available :")
    return coin_processor(order)


off = False

while not off:
    choice = input("What would you like ?")
    if choice == "off":
        off = True
    elif choice == "report":
        print(report(MENU["null"], resources))
    elif not sufficient(choice, resources):
        print("'Ingredients Are Not Available'")
    else:
        after_sufficient(choice)
