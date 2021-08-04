from models.order import Order
from models.customer_items import *

order_1 = Order(customer_2, '04/08/2021', 3, 'Ping-pong bats')
order_2 = Order(customer_1, '04/08/2021', 2, 'Ping-pong balls')
order_3 = Order(customer_1, '04/08/2021', 2, 'Ping-pong bats')

orders = [order_1, order_2, order_3]