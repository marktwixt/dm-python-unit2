from flask import Flask, render_template, request, redirect, url_for
from cupcakes import get_cupcakes_from_csv, get_cupcake_by_id, get_order_items_from_csv, delete_order_item
from orders import append_order
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cupcakes")
def all_cupcakes():
    cupcakes = get_cupcakes_from_csv("cupcakes.csv")  # Call the function to get the list of cupcakes
    return render_template("cupcakes.html", cupcakes=cupcakes)  # Pass the cupcakes list to the template

@app.route("/cupcake_individual/<int:cupcake_id>")  # variable to represent the cupcake_id
def individual_cupcake(cupcake_id):  # cupcake_id as an argument to the function
    cupcake = get_cupcake_by_id("cupcakes.csv", cupcake_id)  # Call the function to get the cupcake details
    if cupcake:
        return render_template("individual-cupcake.html", cupcake=cupcake)  # Pass the cupcake object to the template
    else:
        return "Cupcake not found", 404

@app.route("/order")
def order():
    cupcakes = get_cupcakes_from_csv("cupcakes.csv")  # Get the list of cupcakes
    return render_template("order.html", cupcakes=cupcakes)  # Pass the cupcakes list to the template

@app.route("/add_to_order", methods=["POST"])
def add_to_order():
    cupcake_id = int(request.form["cupcake_id"])
    quantity = int(request.form["quantity"])

    cupcake = get_cupcake_by_id("cupcakes.csv", cupcake_id)
    if cupcake:
        total_price = float(cupcake["price"]) * quantity
        order = {
            "cupcake_id": cupcake_id,
            "name": cupcake["name"],
            "price": cupcake["price"],
            "quantity": quantity,
            "total_price": total_price,
        }
        append_order("current-order.csv", order)  # Call the append_order function to add the order to the CSV file
        return redirect(url_for("confirmation"))  # Redirect the user to the confirmation page
    else:
        return "Cupcake not found", 404

@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html")

@app.route("/shopping_cart")
def shopping_cart():
    order_items = get_order_items_from_csv("current-order.csv")
    order_total = sum(item.total_price for item in order_items)
    
    # debug
    print("Order items:", order_items)
    print("Order total:", order_total)

    return render_template("shopping_cart.html", order_items=order_items, order_total=order_total)

@app.route("/delete_from_cart/<int:item_id>", methods=["POST"])
def delete_from_cart(item_id):
    delete_order_item("current-order.csv", item_id)
    return redirect(url_for("shopping_cart"))

if __name__ == "__main__":
    app.env = "development"
    app.run(debug=True, port=4004, host="localhost")