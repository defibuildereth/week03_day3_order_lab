from models.order import Order
from models.customer_items import *
from models.product_list import *

order_1 = Order(customer_2, '04/08/2021', 3, product_1)
order_2 = Order(customer_1, '04/08/2021', 2, product_2)
order_3 = Order(customer_1, '04/08/2021', 2, product_1)

orders = [order_1, order_2, order_3]