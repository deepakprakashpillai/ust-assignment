class OrderProcessingSystem:
    def __init__(self):
        self.orders = []

    def add_order(self, customer_name, order_item):
        order = {
            'customer_name': customer_name,
            'order_item': order_item
        }
        self.orders.append(order)
        print(f"Order for {customer_name} has been added.")

    def process_order(self):
        if not self.orders:
            print("No orders to process.")
            return
        
        order = self.orders.pop(0)
        print(f"Processing order for {order['customer_name']}...")
        self.notify_customer(order)

    def notify_customer(self, order):
        print(f"Order for {order['customer_name']} is ready for delivery.")


s= OrderProcessingSystem()

s.add_order('Alice', 'Book')
s.add_order('Bob', 'Laptop')

s.process_order()
s.process_order()
s.process_order()
