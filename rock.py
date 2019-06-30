import pygame
from pygame.locals import *
import subprocess
output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
resolution_x, resolution_y = int(output.decode("utf-8").split("x")[0]), int(output.decode("utf-8").split("x")[1])
pygame_y = resolution_y - int(resolution_y / 5)
pygame_x = pygame_y / 12.0 * 16.0

class Rock:
    def __init__(self, img, x, y):
        self.img = img
        self.x = x * int(pygame_x / 16.0)
        self.y = y * int(pygame_y / 12.0)
        pygame.init()

    def get_image(self):
        img_surface = pygame.Surface((int(pygame_x / 16.0)-2, int(pygame_y / 12.0))-2, pygame.SRCALPHA, 32)
        img_surface = img_surface.convert_alpha()
        img_surface.blit(self.img, (0, 0))
        return img_surface

    