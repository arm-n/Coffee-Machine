MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

# Initial ingredient stock
water = 500
milk = 500
coffee = 300
profit = 0.0  # Store total earnings

def update_ingredients(ask):
    global water, milk, coffee  # Updating the global ingredient values
    required = MENU[ask]["ingredients"]

    if required.get("water", 0) > water:
        print("Sorry, not enough water!")
        return False
    if required.get("milk", 0) > milk:
        print("Sorry, not enough milk!")
        return False
    if required.get("coffee", 0) > coffee:
        print("Sorry, not enough coffee!")
        return False

    # Deduct used ingredients
    water -= required.get("water", 0)
    milk -= required.get("milk", 0)
    coffee -= required.get("coffee", 0)

    return True  # Ingredients were successfully updated

while True:
    ask = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if ask == "report":
        print(f"\nWater: {water} ml")
        print(f"Milk: {milk} ml")
        print(f"Coffee: {coffee} g")
        print(f"Total Profit: ${profit:.2f}")  # Display total earnings
        continue  # Keep running after showing the report

    if ask == "exit":
        print("Turning off the coffee machine. Have a great day! ☕")
        break  # Exit the loop

    if ask not in MENU:
        print("Invalid selection. Please choose espresso, latte, cappuccino, report, or exit.")
        continue

    cost = MENU[ask]["cost"]

    # Check if enough ingredients are available
    if not update_ingredients(ask):
        continue  # Skip the coin process if ingredients are insufficient

    print(f"The ordered coffee is {ask} and it costs ${cost}")
    print("Please insert coins.")

    # Coin processing
    quarter = 0.25
    dime = 0.1
    penny = 0.01
    nickel = 0.05

    given_quarter = int(input("How many Quarters: "))
    given_dime = int(input("How many Dimes: "))
    given_penny = int(input("How many Pennies: "))
    given_nickel = int(input("How many Nickels: "))

    def given_coins():
        total = (given_quarter * quarter) + (given_dime * dime) + (given_penny * penny) + (given_nickel * nickel)
        return total

    total_money = given_coins()
    print(f"Total inserted money: ${total_money:.2f}")

    if total_money >= cost:
        change = total_money - cost
        if change > 0:
            print(f"Here is your change: ${change:.2f}")
        print(f"Enjoy your {ask}! ☕")  # Coffee is served
        profit += cost  # Update profit after successful purchase
    else:
        print("Insufficient funds. Money refunded")
