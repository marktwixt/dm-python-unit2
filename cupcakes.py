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
    
def get_cupcake_by_id(file, cupcake_id):
    cupcakes = get_cupcakes_from_csv(file)
    try:
        return cupcakes[cupcake_id - 0]  # Assuming the cupcake_id starts from 1
    except IndexError:
        return None
    
def get_cupcakes_from_csv(file):
    cupcakes = []
    with open(file, newline="\n") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            row["sprinkles"] = row["sprinkles"].split("|")
            cupcakes.append(row)
    return cupcakes

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["name", "price", "flavor", "frosting", "sprinkles", "filling", "size"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for cupcake in cupcakes:
            cupcake_dict = {
                "name": cupcake.name,
                "price": cupcake.price,
                "flavor": cupcake.flavor,
                "frosting": cupcake.frosting,
                "sprinkles": "|".join(cupcake.sprinkles),
                "filling": cupcake.filling,
                "size": cupcake.size,
            }
            writer.writerow(cupcake_dict)

def append_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["name", "price", "flavor", "frosting", "sprinkles", "filling", "size"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        cupcake_dict = {
            "name": cupcake.name,
            "price": cupcake.price,
            "flavor": cupcake.flavor,
            "frosting": cupcake.frosting,
            "sprinkles": "|".join(cupcake.sprinkles),
            "filling": cupcake.filling,
            "size": cupcake.size,
        }
        writer.writerow(cupcake_dict)

if __name__ == "__main__":
    # Create a list of cupcake instances
    cupcakes = [
        Mini("Chocolate Dream", 2.50, "chocolate", "chocolate", ""),
        Mini("Vanilla Delight", 2.50, "vanilla", "vanilla", ""),
        Mini("Strawberry", 2.50, "strawberry", "strawberry", ""),
        Large("Chocolate Dream", 4.50, "chocolate", "chocolate", ""),
        Large("Vanilla Delight", 4.50, "vanilla", "vanilla", ""),
        Large("Strawberry", 4.50, "strawberry", "strawberry", "")
    ]

    # Write the new CSV file with the list of cupcakes
    write_new_csv("cupcakes.csv", cupcakes)

    # Append a new cupcake to the existing CSV file
    new_cupcake = Large("Red Velvet", 4.50,
                        "red velvet", "cream cheese", "")
    append_cupcake("cupcakes.csv", new_cupcake)

    # Read the CSV file to verify the cupcakes have been added
    get_cupcakes_from_csv("cupcakes.csv")
