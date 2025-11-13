from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# ------------------------------------
# Database Connection
# ------------------------------------
db = mysql.connector.connect(
    host="localhost",
    user="root",         # change if needed
    password="root",     # your MySQL password
    database="food_order"  # your database name (matches your SQL script)
)

# ------------------------------------
# Home Route
# ------------------------------------
@app.route('/')
def home():
    return """
    <h2>Welcome!</h2>
    <p><a href='/users'>View Users</a></p>
    <p><a href='/restaurants'>View Restaurants</a></p>
    <p><a href='/menu_items'>View Menu Items</a></p>
    <p><a href='/orders'>View Orders</a></p>
    <p><a href='/payments'>View Payments</a></p>
    <p><a href='/delivery_staff'>View Delivery Staff</a></p>
    """

# ------------------------------------
# Existing Routes
# ------------------------------------
@app.route('/menu_items')
def show_menu_items():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM menu_items;")
    data = cursor.fetchall()
    cursor.close()
    return render_template('menu_items.html', data=data)

@app.route('/ordered_items')
def show_ordered_items():
    # ⚠️ NOTE: ordered_items table doesn’t exist in your SQL script.
    # We’ll skip or you can rename this route to /orders (below).
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM orders;")
    data = cursor.fetchall()
    cursor.close()
    return render_template('ordered_items.html', data=data)

@app.route('/delivery_staff')
def show_delivery_staff():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM delivery_staff;")
    data = cursor.fetchall()
    cursor.close()
    return render_template('delivery_staff.html', data=data)

# ------------------------------------
# ✅ NEW ROUTES for missing tables
# ------------------------------------

@app.route('/users')
def show_users():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")
    data = cursor.fetchall()
    cursor.close()
    return render_template('users.html', data=data)

@app.route('/restaurants')
def show_restaurants():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM restaurants;")
    data = cursor.fetchall()
    cursor.close()
    return render_template('restaurants.html', data=data)

@app.route('/orders')
def show_orders():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM orders;")
    data = cursor.fetchall()
    cursor.close()
    return render_template('orders.html', data=data)

@app.route('/payments')
def show_payments():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM payments;")
    data = cursor.fetchall()
    cursor.close()
    return render_template('payments.html', data=data)

# ------------------------------------
# Run App
# ------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
