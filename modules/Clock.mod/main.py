from threading import Timer, Thread
from datetime import datetime
import time

class main:
    def __init__(self):
        self.getTime()
        self.id = "clockMod"
        pass

    def buildButton(self):
        return "<div id = \""+self.id+"\" style = \"text-align:center; display: table-cell; vertical-align: middle;\">"\
                        +self.buttonText()+\
               "</div>"
    
    def buttonText(self):
        return self.day+"<br><div style= 'font-style:strong;font-size:50pt;'>"+self.time+"</div><br>"+self.date

    def onClick(self, screen):
        return "Click Registered"

    def clockMod(self):
        while True:
            Timer(30,self.clockMod)
            self.getTime()
            command = "$('#"+self.id+"').html(\""+self.buttonText()+"\")"
            print(command)
            self.ws.send(command)
            time.sleep(30)
        
        
    def getTime(self):
        array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        dtime = datetime.now()
        self.day = array[dtime.weekday()]
        self.time = dtime.strftime("%H:%M")
        self.date = dtime.strftime("%d %B %Y")
        return dtime

    def setWebSocket(self, websocket):
        self.ws = websocket
        #Need websocket to be set before sending any kind of update command
        Thread(target=self.clockMod).start()

if __name__ == "__main__": 
    mainclass = main()
    print(mainclass.day, mainclass.time, mainclass.date)