from Observers.observers import Observer



class Display(Observer):

    # Display have to register himself to server
    # def register(self, subject):
    #     subject.register(self)

    # def unregister(self, subject):
    #     subject.unregister(self)  

    # let keep both of these method in observer as we might have multiple observers  

    # this display need to register himself to the subject/server 
    def update(self, temp, humidity):
        print(f"Temprature: {temp} and Humidity: {humidity} from display")