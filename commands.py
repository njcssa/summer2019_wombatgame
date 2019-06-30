
import time
class Commands:
    def __init__(self, wombat):
        self.wombat = wombat
        global bob
        bob = self.wombat # change name to whatever you want
        bob.leaves = 1000

    def turn_right(self):
        bob.turn_left()
        bob.turn_left()
        bob.turn_left()

        

    

    def run(self):
        pass
        