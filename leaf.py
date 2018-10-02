import pygame
from pygame.locals import *

class Leaf:
    def __init__(self, img, x, y, num):
        self.img = img
        self.x = x * 50
        self.y = y * 50
        self.num = num
        pygame.init()

    def get_image(self):
        img_surface = pygame.Surface((48, 48), pygame.SRCALPHA, 32)
        img_surface = img_surface.convert_alpha()
        font = pygame.font.SysFont('Sans', 18)
        text = font.render(str(self.num), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (25, 20)
        img_surface.blit(self.img, (0, 0))
        img_surface.blit(text, text_rect)
        return img_surface
