from flask import Flask, render_template
from cupcakes import get_cupcakes_from_csv, get_cupcake_by_id  # Import the new function from cupcakes.py

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cupcakes")
def all_cupcakes():
    cupcakes = get_cupcakes_from_csv("cupcakes.csv")  # Call the function to get the list of cupcakes
    return render_template("cupcakes.html", cupcakes=cupcakes)  # Pass the cupcakes list to the template

@app.route("/cupcake_individual/<int:cupcake_id>")  # Add a variable to represent the cupcake_id
def individual_cupcake(cupcake_id):  # Add cupcake_id as an argument to the function
    cupcake = get_cupcake_by_id("cupcakes.csv", cupcake_id)  # Call the function to get the cupcake details
    if cupcake:
        return render_template("individual-cupcake.html", cupcake=cupcake)  # Pass the cupcake object to the template
    else:
        return "Cupcake not found", 404

@app.route("/order")
def order():
    return render_template("order.html")

if __name__ == "__main__":
    app.env = "development"
    app.run(debug=True, port=4004, host="localhost")