class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def get_order_by_name(self, customer):
        return [
            order["order"]
            for order in self.orders
            if order["name"] == customer
        ]

    def add_new_order(self, customer, order, day):
        self.orders.append({"name": customer, "order": order, "day": day})

    def get_most_ordered_dish_per_customer(self, customer):
        total = self.get_order_by_name(customer)
        return max(set(total), key=total.count)

    def get_never_ordered_per_customer(self, customer):
        total = set(self.get_order_by_name(customer))
        return {order["order"] for order in self.orders}.difference(total)

    def get_days_never_visited_per_customer(self, customer):
        total = [
            order["day"]
            for order in self.orders
            if order["name"] == customer
        ]
        return {order["day"] for order in self.orders}.difference(total)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
