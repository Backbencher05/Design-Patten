from Observers.observers import Observer


class Zomato(Observer):
    def update(self, temp, humidity):
        if humidity > 20:
            print("Zomato updated price of delivery..")

        if humidity <=20:
            print("Zomato updated price increased already increase of delivery..")
