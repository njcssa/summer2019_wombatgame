
import time
class Commands:
    def __init__(self, wombat):
        self.wombat = wombat
        global bob
        bob = self.wombat # change name to whatever you want
        bob.leaves = 1000
    

    def run(self):
        bob.walk()
        bob.walk()
        bob.walk()

        
        