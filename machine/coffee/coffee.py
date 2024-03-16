class Coffee:
    def __init__(self, name, water, milk, coffee_beans, price):
        self.name = name
        self.ingredients = {"water": water, "milk": milk, "coffee_beans": coffee_beans}
        self.price = price

    def get_ingredients(self):
        print(f"Ingredients for {self.name}:")
        for ingredient, amount in self.ingredients.items():
            print(f"{ingredient.capitalize()}: {amount} {'ml' if ingredient in ['water', 'milk'] else 'g'}")
        print(f"Price: ${self.price}")

    def make_coffee(self):
        print(f"Making {self.name} coffee...")
        # Add your logic for making the coffee here


class Espresso(Coffee):
    def __init__(self):
        super().__init__("Espresso", 250, 0, 16, 4)


class Latte(Coffee):
    def __init__(self):
        super().__init__("Latte", 350, 75, 20, 7)


class Cappuccino(Coffee):
    def __init__(self):
        super().__init__("Cappuccino", 200, 100, 12, 6)
