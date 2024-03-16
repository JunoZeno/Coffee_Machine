from coffee.coffee import Coffee


class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, total_money, disposable_cups):
        """
        Initializes the CoffeeMachine class with the given parameters.

        Args:
            water (int): The amount of water in the machine.
            milk (int): The amount of milk in the machine.
            coffee_beans (int): The amount of coffee beans in the machine.
            total_money (float): The total money in the machine.
            disposable_cups (int): The number of disposable cups in the machine.
        """
        self.amount_of_ingredients_in_machine: dict = {"water": water, "milk": milk, "coffee_beans": coffee_beans}
        self.total_money: float = total_money
        self.disposable_cups: int = disposable_cups
        self.one_cup_coffee_ingredients = None

        while True:
            user_choice = input("\nWrite action (buy, fill, take, remaining, exit):\n").strip().lower()

            if user_choice == "buy":
                self.buy_coffee()
            elif user_choice == "fill":
                self.fill_machine()
            elif user_choice == "take":
                self.take_money()
            elif user_choice == "remaining":
                print(self)
            elif user_choice == "exit":
                break
            else:
                print("Invalid choice")

    def buy_coffee(self):
        """
        Allows the user to buy a cup of coffee.

        The user is prompted to choose a type of coffee (espresso, latte, or cappuccino).
        If the user enters an invalid choice, they are prompted again until a valid choice is made.
        Once a valid choice is made, the method checks if the machine can make the chosen coffee.
        If it can, the coffee is made and the method ends.
        If it can't, the user is informed and the method ends.
        """
        selection_complete = False
        while not selection_complete:
            user_coffee = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main "
                                "menu:\n")

            if str(user_coffee).lower().strip() == "back":
                break

            try:
                user_coffee = int(user_coffee)
            except ValueError:
                print("Invalid choice")
                continue

            if user_coffee == 1:
                espresso = Espresso()
                self._can_make_coffee(espresso.ingredients, espresso.price)
                selection_complete = True
            elif user_coffee == 2:
                latte = Latte()
                self._can_make_coffee(latte.ingredients, latte.price)
                selection_complete = True
            elif user_coffee == 3:
                cappuccino = Cappuccino()
                self._can_make_coffee(cappuccino.ingredients, cappuccino.price)
                selection_complete = True
            else:
                print("Invalid choice")

    def fill_machine(self):
        """
           Fills the coffee machine with the specified amounts of water, milk, coffee beans, and disposable cups.

           The user is prompted to enter the amount of each ingredient they want to add.
           The entered amounts are then added to the current amounts in the coffee machine.
        """
        water = int(input("\nWrite how many ml of water you want to add:\n> "))
        milk = int(input("Write how many ml of milk you want to add:\n> "))
        coffee_beans = int(input("Write how many grams of coffee beans you want to add:\n> "))
        disposable_cups = int(input("Write how many disposable cups you want to add:\n> "))

        self.amount_of_ingredients_in_machine["water"] += water
        self.amount_of_ingredients_in_machine["milk"] += milk
        self.amount_of_ingredients_in_machine["coffee_beans"] += coffee_beans
        self.disposable_cups += disposable_cups

    def take_money(self):
        """
        Allows the user to take all the money from the coffee machine.

        The total amount of money in the machine is printed and then set to zero.
        """
        print(f"I gave you ${self.total_money}")
        self.total_money = 0

    def _sum_of_machine_ingredients(self):
        """
        Calculates the total sum of all ingredients in the coffee machine.

        This method iterates over the values in the `amount_of_ingredients_in_machine` dictionary and sums them up.
        The sum represents the total quantity of all ingredients in the machine.

        Returns:
            int: The sum of all ingredients in the coffee machine.
        """
        return sum(self.amount_of_ingredients_in_machine.values())

    def _can_make_coffee(self, list_of_ingredients_needed: dict, coffee_price: int):  # KEEP
        """
        Checks if the coffee machine has enough ingredients to make the desired amount of coffee.
        If there are enough ingredients, it prints a message indicating the number of cups that can be made.
        If there are not enough ingredients, it prints a message indicating the maximum number of cups that can be made.
        """
        if self._sum_of_machine_ingredients() == 0:
            print("No, I can make only 0 cups of coffee")
            return

        if self.disposable_cups == 0:
            print("No, I can make only 0 cups of coffee")
            return

            left_over_ingredients = {}
            for key, value in self.amount_of_ingredients_in_machine.items():
                if value >= self.amount_of_ingredients_needed[key]:
                    left_over_ingredients[key] = value - self.amount_of_ingredients_needed[key]
                else:
                    cups = self._enough_ingredients_to_make_coffee(self.amount_of_ingredients_in_machine,
                                                                   self.one_cup_coffee_ingredients)
                    print(f"No, I can make only {cups} cups of coffee")
                    return

            extra_cups = self._enough_ingredients_to_make_coffee(left_over_ingredients, self.one_cup_coffee_ingredients)
            if extra_cups > 0:
                print(f"Yes, I can make that amount of coffee (and even {extra_cups} more than that)")
            else:
                print("Yes, I can make that amount of coffee")

    def _enough_ingredients_to_make_coffee(self, amount_of_ingredients_in_machine, amount_of_ingredients_needed) -> int:
            """
            Checks if there are enough ingredients in the coffee machine to make X cups of coffee.

            Args:
                amount_of_ingredients_in_machine (dict): A dictionary representing the amount of each ingredient in the machine.
                amount_of_ingredients_needed (dict): A dictionary representing the amount of each ingredient needed to make coffee.

            Returns:
                int: The maximum number of cups of coffee that can be made with the available ingredients.
            """

            enough_contents = True
            cups_mach_can_make = 0
            cups = 1
            while enough_contents:
                enough_contents = all(
                    amount_of_ingredients_in_machine[key] >= amount_of_ingredients_needed[key] * cups
                    for key in amount_of_ingredients_needed
                )
                if enough_contents:
                    cups_mach_can_make = cups
                    cups += 1

            return cups_mach_can_make

    def __str__(self):
        return f"Water: {self.amount_of_ingredients_in_machine['water']}\n" \
               f"Milk: {self.amount_of_ingredients_in_machine['milk']}\n" \
               f"Coffee Beans: {self.amount_of_ingredients_in_machine['coffee_beans']}\n" \
               f"Cups: {self.cups_needed}\n" \
               f"Cost: {self.cost}"


if __name__ == "__main__":
    water_needed = int(input("Write how many ml of water the coffee machine has:\n"))
    milk_needed = int(input("Write how many ml of milk the coffee machine has:\n"))
    coffee_beans_needed = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
    cups_needed = int(input("Write how many cups of coffee you will need:\n"))

    coffee_machine = CoffeeMachine(water_needed, milk_needed, coffee_beans_needed, cups_needed)
    coffee_machine.check_machine_resources()
