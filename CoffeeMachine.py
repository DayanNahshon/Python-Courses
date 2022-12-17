MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def IsResourcesSufficient(OrderIngredients):
    """"Returns True when order can be made, False if ingredients are insufficient."""
    for item in OrderIngredients:
        if OrderIngredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def ProcessCoins():
    """"Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def IsTransactionSuccessful(MoneyReceived, DrinkCost):
    """"Return True when the payment is accepted, or False if money is insufficient."""
    if MoneyReceived >= DrinkCost:
        change = round(MoneyReceived - DrinkCost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += DrinkCost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
  
def MakeCoffe(DrinkName, OrderIngredients):
    """Deduct the required ingredients from the resources."""
    for item in OrderIngredients:
        resources[item] -= OrderIngredients[item]
    print(f"Here is your {DrinkName}. Enjoy! ☕")

isOn = True

while isOn:
    UserChoice = input("What would you like? (espresso/latte/cappuccino): ")
    if UserChoice == "off":
        isOn = False
    elif UserChoice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[UserChoice]
        if IsResourcesSufficient(drink["ingredients"]):
            payment = ProcessCoins()
            if IsTransactionSuccessful(payment, drink["cost"]):
                MakeCoffe(UserChoice, drink["ingredients"])


