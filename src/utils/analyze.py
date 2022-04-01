import csv
from collections import Counter


def orders_file(path):
    with open(path) as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        return [row for row in reader]


def maria(orders):
    order = [order[1] for order in orders if order[0] == "maria"]
    return list(Counter(order))[0]


def arnaldo(orders):
    order = [order[1] for order in orders if order[0] == "arnaldo"]
    return order.count("hamburguer")


def joao(orders, joao_orders):
    return {order[1] for order in orders if order[1] not in joao_orders}


def days_joao(days, joao_days):
    return {day[2] for day in days if day[2] not in joao_days}
