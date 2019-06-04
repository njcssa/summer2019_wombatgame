import pygame
from pygame.locals import *
from world import World
from wombat import Wombat
from commands import Commands
from time import sleep


# public vars
screen = pygame.display.set_mode((800, 600))
wombat_img = pygame.image.load('wombat.png')
wombat_img = pygame.transform.scale(wombat_img, (50, 50))


# creating objects
wombat = Wombat(wombat_img, 0, 0) # num params are for starting location
delay = 0.05 # amount of time delay
world = World(screen.get_size(), wombat, screen, delay, 0)
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
