import threading
import time
import sched
import datetime

class clockThread:
    def __init__(self, button):
        self.button = button    
    
    def update(self):
        x = datetime.datetime.now()
        self.button.text = x.strftime("%A %d %B\n%H:%M")
        print(x.strftime("%A %d %B\n%H:%M"))
        
    def clock(self):
        while 1:
            threading.Timer(60,self.clock)
            self.update()
            time.sleep(30)



if __name__ == "__main__":
    t = clockThread("test")
    threading.Thread(target=t.clock).start()
