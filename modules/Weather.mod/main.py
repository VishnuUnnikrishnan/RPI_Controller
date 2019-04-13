'''
Main Class for clock
'''
from threading import Timer, Thread
import json
import pyowm
import time

class main:
    def __init__(self):
        self.setVariables()
        self.weather = pyowm.OWM(self.api)

    def buildButton(self):
        html = """<div id = "WeatherMod" style = "text-align:center; display: table-cell; vertical-align: middle;">""" +self.htmlElement()+ """</div>"""
        print(html)
        return html
    
    def htmlElement(self, data=None):
        temp = "20&#8451;"
        image = "/svg/wi-alien.svg"
        weather = {"Thunderstorm":"wi-day-thunderstorm.svg", "Rain":"wi-day-rain.svg", "Snow":"wi-day-snow.svg", "Drizzle":"wi-day-sprinkle.svg", \
            "Clear":"wi-day-sunny.svg", "Clouds":"wi-cloudy.svg"}
        
        if data is not None:
            temp = str(self.temp["temp"])+"&#8451;"
            image = "/svg/"+weather[self.status]
            

        html = """<div style = "font-size:20pt;">"""+temp+"</div><img width=\"100px\" height=\"100px\" src=\""+image+"\"/>"

        return html
    
    
    def onClick(self, screen):
        return "Click Registered"

    def getWeather(self):
        location = self.settings["city"]+","+self.settings["country"]
        observation = self.weather.weather_at_place(location)
        w = observation.get_weather()
        self.temp = w.get_temperature('celsius')
        self.status = w.get_status()
        self.ws.send("""$('#WeatherMod').html(\'"""+self.htmlElement(data = 1)+"""\');""")
        print(self.temp, self.status)
        

    def setVariables(self):
        with open("modules/Weather.mod/weather.secrets","r") as f:
            secrets = json.load(f)
            self.api = secrets["apiKey"]
        with open("modules/Weather.mod/settings.json","r") as f2:
            self.settings = json.load(f2)

    def setCallback(self):
        while True:
            t= Timer(10800,self.setCallback)
            t.start()
            self.getWeather()
            time.sleep(10800)
        

    def setCallbackThread(self):
        Thread(target=self.setCallback).start()

    def setWebSocket(self, websocket):
        self.ws = websocket
        self.setCallbackThread()
    
def test():
    m = main()


class screen:
    def __init__(self):
        pass

    def buildScreen(self):
        return """
                    <div class="modal" id="myModal" tabindex="-1" role="dialog" aria-hidden="true">
                        <div class="modal-dialog modal-full" role="document">
                            <div class="modal-content">
                            ...
                            </div>
                        </div>
                    </div>    
                """

if __name__ == "__main__":
    test()