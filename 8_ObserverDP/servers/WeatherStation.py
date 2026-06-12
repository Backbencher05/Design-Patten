from servers.server import Server


class WeatherStation(Server):
    def __init__(self):
        super().__init__() #all the init data of parent class came here
        self.temp = 0
        self.hum = 0

    def updateWeather(self, temp,hum):
        self.temp = temp
        self.hum = hum
        # if temp and hum. got updated notify the observer 
        self.notify(temp, hum)  