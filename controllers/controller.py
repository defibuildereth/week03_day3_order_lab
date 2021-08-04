from app import app
from flask import render_template
from models.order_list import orders

@app.route('/')
def index():
    return render_template('index.html', orders = orders)