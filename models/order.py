class Order():

    def __init__(self, customer_object, order_date, quantity, product_object):
        self.customer_object = customer_object
        self.order_date = order_date
        self.quantity = quantity
        self.product_object = product_object