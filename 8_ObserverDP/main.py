from servers.WeatherStation import WeatherStation
from Observers.display import Display
from Observers.zomato import Zomato

if __name__ == '__main__':
    ws = WeatherStation()  # we got the weather station server 

    # Now Display and Zomato are observer 
    d1 = Display()
    z = Zomato()

    # we need to tell to server we are your observer , we need to register to the server
    d1.registerSubject(ws)
    z.registerSubject(ws)

    ws.updateWeather(10,30)