'''
Main Class for clock
'''
from threading import Timer

class main:
    def __init__(self):
        
        pass

    def buildButton(self):
        return """<div id = "quote" style = "text-align:center; display: table-cell; vertical-align: middle;">
        <div style ="font-size:20pt; font-style:strong;">I am the master of my fate,<br> I am the captain of my soul. </div>
        </div>"""
    
    def onClick(self, screen):
        return "Click Registered"

    def timeout(self):
        self.ws.send("console.log('Hello World!')")
        


    def setWebSocket(self, websocket):
        self.ws = websocket
        t = Timer(1, self.timeout)
        t.start()
    
    

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

