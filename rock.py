import pygame
from pygame.locals import *

class Rock:
    def __init__(self, img, x, y):
        self.img = img
        self.x = x * 50
        self.y = y * 50
        pygame.init()

    def get_image(self):
        img_surface = pygame.Surface((48, 48), pygame.SRCALPHA, 32)
        img_surface = img_surface.convert_alpha()
        img_surface.blit(self.img, (0, 0))
        return img_surface

    