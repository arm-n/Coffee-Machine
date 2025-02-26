Coffee Machine Project
This is a simple Python-based coffee machine simulation that allows users to order coffee, insert coins, and check their remaining stock of ingredients. The machine can prepare three types of coffee: Espresso, Latte, and Cappuccino. It also tracks profit and updates ingredient stock after each order.

Features
Menu: Users can choose between three types of coffee:
Espresso
Latte
Cappuccino
Stock Management: Tracks the stock of water, milk, and coffee beans.
Profit Tracking: The machine tracks the total earnings from each order.
User Interaction:
The user can check a report showing the current stock of ingredients and the total profit.
Users can input the number of coins they want to insert to make a payment.
The program will inform the user if there aren't enough ingredients or if the funds are insufficient.
Order System: After a successful payment, the ordered coffee is served, and the ingredients are deducted from the stock.
Installation
No installation is required to run this script. Simply clone the repository and run the Python file.

Clone the repository:

bash
Copy
Edit
git clone https://github.com/arm-n/Coffee-Machine.git
Navigate to the project folder:

bash
Copy
Edit
cd Coffee-Machine
Run the program:

bash
Copy
Edit
python main.py
Usage
The program runs in an infinite loop, where you can interact by choosing one of the following options:

Espresso: Orders an espresso for $1.5, which requires 50ml of water and 18g of coffee.
Latte: Orders a latte for $2.5, which requires 200ml of water, 150ml of milk, and 24g of coffee.
Cappuccino: Orders a cappuccino for $3.0, which requires 250ml of water, 100ml of milk, and 24g of coffee.
Report: Displays the current stock of ingredients (water, milk, coffee) and the total profit earned.
Exit: Turns off the coffee machine and exits the program.
You can also input coins (quarters, dimes, pennies, and nickels) to pay for your order. The program will provide change if you overpay, or refund your money if you don't provide enough.

Example Interaction
pgsql
Copy
Edit
What would you like? (espresso/latte/cappuccino): espresso
The ordered coffee is espresso and it costs $1.50
Please insert coins.
How many Quarters: 2
How many Dimes: 1
How many Pennies: 0
How many Nickels: 0
Total inserted money: $0.70
Insufficient funds. Money refunded

What would you like? (espresso/latte/cappuccino): latte
The ordered coffee is latte and it costs $2.50
Please insert coins.
How many Quarters: 3
How many Dimes: 0
How many Pennies: 0
How many Nickels: 0
Total inserted money: $0.75
Insufficient funds. Money refunded
Contributing
Feel free to fork this repository and make improvements! If you find any issues or bugs, please feel free to submit an issue.

Fork the repository.
Create a new branch (git checkout -b feature-name).
Make your changes and commit them (git commit -am 'Add feature').
Push to your branch (git push origin feature-name).
Create a new pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.
