import pygame
from pygame.locals import *
from world import World
from wombat import Wombat
from commands import Commands
# from commands import Commands - only use this for student version
#from commands import Commands
from time import sleep

# gets the screen resolution for dynamic scaling
import subprocess
output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
resolution_x, resolution_y = int(output.decode("utf-8").split("x")[0]), int(output.decode("utf-8").split("x")[1])
pygame_y = resolution_y - int(resolution_y / 5)
pygame_x = pygame_y / 12.0 * 16.0


# public vars
screen = pygame.display.set_mode((int(pygame_x), int(pygame_y)))
wombat_img = pygame.image.load('wombat.png')
wombat_img = pygame.transform.scale(wombat_img, (int(pygame_x / 16.0), int(pygame_y / 12.0)))


# creating objects
wombat = Wombat(wombat_img, 0, 1) # num params are for starting location
delay = 0.5 # amount of time delay
setup = 0 # setup of world
world = World(screen.get_size(), wombat, screen, pygame_x, pygame_y, delay, setup)
commands = Commands(wombat)
# add some variables to wombat
wombat.world = world
wombat.tile_objects = world.tile_objects


# starting background
world.display()
sleep(0.5)



def main():
    commands.run() # running user code, might run into problems if infinite loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        world.display()

if __name__ == '__main__': main()
