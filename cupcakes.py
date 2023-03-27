import csv
from pprint import pprint
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

    def __init__(self, name, price, flavor, frosting, filling):
        super().__init__(name, price, flavor, frosting, filling)

    def calculate_price(self, quantity):
        return quantity * self.price


class Large(Cupcake):
    size = "large"

    def __init__(self, name, price, flavor, frosting, filling):
        super().__init__(name, price, flavor, frosting, filling)

    def calculate_price(self, quantity):
        return quantity * self.price

def read_csv(file):
    with open(file, newline="\n") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            row["sprinkles"] = row["sprinkles"].split("|")
            pprint(row)

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for cupcake in cupcakes:
            cupcake_dict = {
                "size": cupcake.size,
                "name": cupcake.name,
                "price": cupcake.price,
                "flavor": cupcake.flavor,
                "frosting": cupcake.frosting,
                "sprinkles": "|".join(cupcake.sprinkles),
                "filling": cupcake.filling,
            }
            writer.writerow(cupcake_dict)

def append_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        cupcake_dict = {
            "size": cupcake.size,
            "name": cupcake.name,
            "price": cupcake.price,
            "flavor": cupcake.flavor,
            "frosting": cupcake.frosting,
            "sprinkles": "|".join(cupcake.sprinkles),
            "filling": cupcake.filling,
        }
        writer.writerow(cupcake_dict)

if __name__ == "__main__":
    # Create a list of cupcake instances
    cupcakes = [
        Mini("Mini Chocolate Dream", 2.50, "chocolate", "chocolate", None),
        Mini("Mini Vanilla Delight", 2.50, "vanilla", "vanilla", None),
        Mini("Mini Strawberry", 2.50, "strawberry", "strawberry", None),
        Large("Large Chocolate Dream", 4.50, "chocolate", "chocolate", None),
        Large("Large Vanilla Delight", 4.50, "vanilla", "vanilla", None),
        Large("Large Strawberry", 4.50, "strawberry", "strawberry", None)
    ]

    # Write the new CSV file with the list of cupcakes
write_new_csv("cupcakes.csv", cupcakes)

# Append a new cupcake to the existing CSV file
new_cupcake = Large("Large Red Velvet", 4.50,
                    "red velvet", "cream cheese", None)
append_cupcake("cupcakes.csv", new_cupcake)

# Read the CSV file to verify the cupcakes have been added
read_csv("cupcakes.csv")
