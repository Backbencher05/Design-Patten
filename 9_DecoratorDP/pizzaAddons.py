# if we are addingAddons, Pizza will be there
from pizza import Pizza

class PizzaAddons(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_price(self):
        return self.pizza.get_price()  # let we don't want any addons