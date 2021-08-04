from app import app
from flask import render_template
from models.order_list import orders

@app.route('/order')
def index():
    return render_template('index.html', orders = orders)

@app.route('/order/<index>')
def one_by_index(index):
    return render_template('order_by_index.html', order = orders[int(index)-1])

@app.route('/order/name/<name>')
def one_by_name(name):
    relevant_order = []
    for order in orders:
        if order.customer_object.name.lower() == name.lower():
            relevant_order.append(order)
    print(f'{len(relevant_order)}!!!!!!!!!!!!!!!!!!')
    return render_template('order_by_name.html', orders = relevant_order)