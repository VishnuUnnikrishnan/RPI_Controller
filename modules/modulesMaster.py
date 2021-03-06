import json
import os
import imp

class display:
    def __init__(self):
        with open("settings/settings.json") as f:
            self.settings = json.load(f)
            self.paths = []
            self.createPaths()
            self.buttonModules = []
            self.screenModules = []
    
    def createOutput(self):
        rows = int(self.settings["main_settings"]["row"])
        cols = int(self.settings["main_settings"]["col"])
        retString = ""
        k = 0
        for i in range(0,rows):
            retString += "<div class='row baseRow'>"
            for j in range(0,cols):
                #Should only have 1,2,3,4,6,12 columns, too lazy to handle centering otherwise
                num_cols=int(12)/int(cols)
                retString += "<div class='col-sm-"+str(round(num_cols))+" baseCol' id='"+str(k)+"' onClick='buttonPress("+str(id)+")' >"
                #This is where the code to load modules is located
                try:
                    moduleClass = self.loadModule(k)
                    newModule = moduleClass()
                    self.buttonModules.append(newModule)
                    retString += newModule.buildButton()

                except Exception as e:
                    retString += "Error " + str(e)
                retString += "</div>"
                k+=1
            retString += "</div>"
            print("Paths: "+str(self.paths))
            

        return retString
    
    def loadModule(self, id):
        if id >= len(self.paths):
            id = 0
        module = imp.load_source("main","modules/"+self.paths[id]+"/main.py")
        executeClass = getattr(module, "main")

        return executeClass

    def createPaths(self):
        rawDir = next(os.walk('./modules'))[1] 
        self.paths = [x for x in rawDir if x.endswith(".mod")]
        self.paths.sort()

    def setLink(self, ws):
        self.ws = ws
        print(self.paths)
        print(self.buttonModules)
        for i in range(0,len(self.paths)):
            self.buttonModules[i].setWebSocket(self.ws)
        

