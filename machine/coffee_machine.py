from coffee.coffee import Coffee


class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, cups, cost=0):
        self.cups_needed: int = cups
        self.amount_of_ingredients_in_machine = {"water": water, "milk": milk, "coffee_beans": coffee_beans}
        self.cost: float = cost

        self.new_coffee = None
        self.one_cup_coffee_ingredients = {"water": 200, "milk": 50, "coffee_beans": 15}
        self.amount_of_ingredients_needed = {}

    def check_machine_resources(self):
        # Check if the machine has enough resources to make the coffee
        self._calculate_ingredients_needed(self.one_cup_coffee_ingredients, self.cups_needed)
        self._check_if_zero_cups()
        self._can_make_coffee()

    def brew_coffee(self):
        # new_coffee = Coffee()
        pass

    def _calculate_ingredients_needed(self, one_cup_ingredients: dict, cups_to_make: int):
        """
        Calculates the amount of ingredients needed to make a specified number of cups of coffee.

        Args:
            one_cup_ingredients (dict): A dictionary containing the ingredients needed for one cup of coffee.
            cups_to_make (int): The number of cups of coffee to make.

        Returns:
            None
        """
        for key, value in one_cup_ingredients.items():
            if cups_to_make > 0:
                self.amount_of_ingredients_needed[key] = value * cups_to_make

    def _check_if_zero_cups(self):
            """
            Checks if the number of cups needed is zero and determines if the coffee machine has enough ingredients to make that amount of coffee.

            Returns:
                None
            """
            if self.cups_needed == 0:
                enough_contents = all(
                    self.amount_of_ingredients_in_machine[key] >= self.one_cup_coffee_ingredients[key]
                    for key in self.one_cup_coffee_ingredients
                )
                total_contents = self._sum_of_machine_ingredients()

                if enough_contents:
                    print("Yes, I can make that amount of coffee (and even 1 more than that)")
                elif total_contents == 0:
                    print("Yes, I can make that amount of coffee ")
                else:
                    print("No, I can't make that amount of coffee")

    def _sum_of_machine_ingredients(self):
            """
            Calculates the total sum of all ingredients in the coffee machine.

            Returns:
                int: The sum of all ingredients in the coffee machine.
            """
            return sum(self.amount_of_ingredients_in_machine.values())

    
    def _can_make_coffee(self):
            """
            Checks if the coffee machine has enough ingredients to make the desired amount of coffee.
            If there are enough ingredients, it prints a message indicating the number of cups that can be made.
            If there are not enough ingredients, it prints a message indicating the maximum number of cups that can be made.
            """
            if self._sum_of_machine_ingredients() == 0 and self.cups_needed > 0:
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
