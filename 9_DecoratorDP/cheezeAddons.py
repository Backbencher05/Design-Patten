from pizzaAddons import PizzaAddons

class Cheese(PizzaAddons):

    def get_price(self):
        return self.pizza.get_price() + 30