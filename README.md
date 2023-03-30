Cupcake Store Web Application

This web application allows users to browse a list of cupcakes, view individual cupcake details, place an order, and manage their shopping cart.

Features:

-Browse all available cupcakes

-View details of individual cupcakes

-Add cupcakes to an order

-View the current shopping cart

-Remove items from the shopping cart

-Confirmation page for successful orders

-Responsive and visually appealing design

Installation:

Clone the repository to your local machine:
git clone https://github.com/marktwixt/dm-python-unit2.git

Install the required dependencies:
Flask==2.1.1

Usage:

Run the server.py file:
python server.py
Open your browser and navigate to http://localhost:4004.

Technologies:

-Python

-Flask

-HTML

-CSS

Project Structure:

-server.py: The main Python file containing the Flask application logic and routes.

-cupcakes.py: A Python module containing functions for reading and writing cupcake data from/to CSV files.

--templates/: A directory containing HTML templates for rendering different pages.
-index.html: The homepage template.
-cupcakes.html: The template for displaying all cupcakes.
-individual-cupcake.html: The template for displaying the details of a specific cupcake.
-order.html: The template for placing an order.
-shopping-cart.html: The template for displaying the user's shopping cart.
-confirmation.html: The template for displaying a confirmation message after a successful order.

--static/: A directory containing static files like stylesheets and images.
-styles.css: The main stylesheet for the application.

-cupcakes.csv: A CSV file containing cupcake data.
-current-order.csv: A CSV file containing the current order data.


Author
Walt Ostrander
