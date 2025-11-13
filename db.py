from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # change this to your MySQL username
        password="",          # change this to your MySQL password
        database="food_order" # make sure this DB exists
    )

# ---------------- USERS ----------------
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """INSERT INTO users (name, email, password, phone_no, address)
               VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(query, (data['name'], data['email'], data['password'], data['phone_no'], data['address']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'User added successfully'})

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)


# ---------------- RESTAURANTS ----------------
@app.route('/restaurants', methods=['POST'])
def add_restaurant():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """INSERT INTO restaurants (name, owner_name, email, phone_no, address, cuisine_type)
               VALUES (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, (data['name'], data['owner_name'], data['email'], data['phone_no'], data['address'], data['cuisine_type']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Restaurant added successfully'})

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM restaurants")
    restaurants = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(restaurants)


# ---------------- MENU ITEMS ----------------
@app.route('/menu_items', methods=['POST'])
def add_menu_item():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """INSERT INTO menu_items (restaurant_id, name, description, category, price, available)
               VALUES (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, (data['restaurant_id'], data['name'], data['description'], data['category'], data['price'], data['available']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Menu item added successfully'})

@app.route('/menu_items', methods=['GET'])
def get_menu_items():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM menu_items")
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(items)


# ---------------- ORDERS ----------------
@app.route('/orders', methods=['POST'])
def add_order():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """INSERT INTO orders (user_id, restaurant_id, item_id, total_amount, delivery_address, order_status)
               VALUES (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, (data['user_id'], data['restaurant_id'], data['item_id'], data['total_amount'], data['delivery_address'], data['order_status']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Order added successfully'})

@app.route('/orders', methods=['GET'])
def get_orders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(orders)


# ---------------- PAYMENTS ----------------
@app.route('/payments', methods=['POST'])
def add_payment():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """INSERT INTO payments (order_id, payment_status, payment_method, amount)
               VALUES (%s, %s, %s, %s)"""
    cursor.execute(query, (data['order_id'], data['payment_status'], data['payment_method'], data['amount']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Payment added successfully'})

@app.route('/payments', methods=['GET'])
def get_payments():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM payments")
    payments = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(payments)


# ---------------- DELIVERY STAFF ----------------
@app.route('/delivery_staff', methods=['POST'])
def add_delivery_staff():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """INSERT INTO delivery_staff (name, phone_no, vehicle_type, current_loc, assigned_order_id, status)
               VALUES (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, (data['name'], data['phone_no'], data['vehicle_type'], data['current_loc'], data['assigned_order_id'], data['status']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Delivery staff added successfully'})

@app.route('/delivery_staff', methods=['GET'])
def get_delivery_staff():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM delivery_staff")
    staff = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(staff)


if __name__ == '__main__':
    app.run(debug=True)
