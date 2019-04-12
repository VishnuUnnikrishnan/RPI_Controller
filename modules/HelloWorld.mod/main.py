'''
Main Class for clock
'''


class main:
    def __init__(self):
        pass

    def buildButton(self):
        return """<div style = "text-align:center; display: table-cell; vertical-align: middle;">
                        Hello World!
                  </div>"""
    
    def onClick(self, screen):
        return "Click Registered"

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

