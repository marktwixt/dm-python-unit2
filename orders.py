import csv

def append_order(file, order):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["name", "quantity", "total_price"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        order_dict = {
            "name": order["name"],
            "quantity": order["quantity"],
            "total_price": order["total_price"],
        }
        writer.writerow(order_dict)