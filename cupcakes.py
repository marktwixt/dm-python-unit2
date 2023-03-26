from abc import ABC, abstractmethod

class Cupcake(ABC):
    size = "regular"

    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod
    def calculate_price(self, quantity):
        pass

class Mini(Cupcake):
    size = "mini"

    def __init__(self, name, price, flavor, frosting):
        super().__init__(name, price, flavor, frosting, None)

    def calculate_price(self, quantity):
        return quantity * self.price

class Large(Cupcake):
    size = "large"

    def __init__(self, name, price, flavor, frosting, filling):
        super().__init__(name, price, flavor, frosting, filling)

    def calculate_price(self, quantity):
        return quantity * self.price * 1.5

class Vegan(Cupcake):
    def __init__(self, name, price, flavor, frosting, filling):
        super().__init__(name, price, flavor, frosting, filling)

    def calculate_price(self, quantity):
        vegan_cost = self.price * 1.2
        return quantity * vegan_cost

class GlutenFree(Cupcake):
    def __init__(self, name, price, flavor, frosting, filling):
        super().__init__(name, price, flavor, frosting, filling)

    def calculate_price(self, quantity):
        gluten_free_cost = self.price * 1.3
        return quantity * gluten_free_cost

if __name__ == "__main__":
    vegan_cupcake = Vegan("Vegan Chocolate Delight", 3.00, "chocolate", "vanilla", "ganache")
    gluten_free_cupcake = GlutenFree("Gluten-Free Chocolate Delight", 3.00, "chocolate", "vanilla", "ganache")

    print(f"Vegan cupcake price for 4 cupcakes: ${vegan_cupcake.calculate_price(4):.2f}")
    print(f"Gluten-free cupcake price for 4 cupcakes: ${gluten_free_cupcake.calculate_price(4):.2f}")
