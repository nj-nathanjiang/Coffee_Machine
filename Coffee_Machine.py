report = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0,
}

prices = {
    "espresso": 1.50,
    "latte": 2.50,
    "cappuccino": 3.00,
}

ingredients = {
    "espresso": {"Water": 50, "Coffee": 18,},
    "latte": {"Water": 200, "Coffee": 24, "Milk": 150,},
    "cappuccino": {"Water": 250, "Coffee": 24, "Milk": 100,},
}


def get_coffee(coffee_type):
    global report
    global num_pennies
    global num_nickels
    global num_dimes
    global num_quarters
    print("Please enter the coins.")
    try:
        num_quarters = int(input("Quarters: "))
        num_dimes = int(input("Dimes: "))
        num_nickels = int(input("Nickels: "))
        num_pennies = int(input("Pennies: "))
    except ValueError:
        num_quarters = 0
        num_dimes = 0
        num_nickels = 0
        num_pennies = 0
    total_money = num_quarters * 0.25 + num_dimes * 0.10 + num_nickels * 0.05 + num_pennies * 0.01
    if total_money > prices[coffee_type]:
        print(f"Here is your change: ${round(total_money - 1.50, 2)}.")
        print(f"Here is your espresso.\nEnjoy!")
        report["Water"] -= ingredients[coffee_type]["Water"]
        report["Coffee"] -= ingredients[coffee_type]["Coffee"]
        report["Money"] += prices[coffee_type]
        try:
            report["Milk"] -= ingredients[coffee_type]["Milk"]
        except KeyError:
            pass
    else:
        print("That is not enough money.")


while True:
    the_input = input("What would you like? "
                      "Type 'report' for a list of the resources. "
                      "Type 'restock' to reload the resources. (espresso/latte/cappuccino/report/restock): ")
    the_input = the_input.lower()
    if the_input == 'report':
        print(f"Water: {report['Water']}ml\n"
              f"Milk: {report['Milk']}ml\n"
              f"Coffee: {report['Coffee']}g\n"
              f"Money: ${report['Money']}")
    elif the_input == 'restock':
        print("Resources restocked.")
        report["Milk"] += 500
        report["Water"] += 500
        report["Coffee"] += 100
    elif the_input == "espresso":
        if report["Water"] < 50:
            print("There isn't enough water.")
            exit()
        elif report["Coffee"] < 18:
            print("There isn't enough coffee.")
            exit()
        get_coffee("espresso")
    elif the_input == "latte":
        if report["Water"] < 200:
            print("There isn't enough water.")
            exit()
        elif report["Coffee"] < 24:
            print("There isn't enough coffee.")
            exit()
        elif report["Milk"] < 150:
            print("There isn't enough milk.")
            exit()
        get_coffee("latte")
    elif the_input == "cappuccino":
        if report["Water"] < 250:
            print("There isn't enough water.")
            exit()
        elif report["Coffee"] < 24:
            print("There isn't enough coffee.")
            exit()
        elif report["Milk"] < 100:
            print("There isn't enough milk.")
            exit()
        get_coffee("cappuccino")
    elif the_input == "exit":
        print("Goodbye")
        exit()
    else:
        print("That is not a coffee.")
