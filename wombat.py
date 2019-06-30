import pygame
from pygame.locals import *
from leaf import Leaf
from rock import Rock

import subprocess
output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
resolution_x, resolution_y = output.decode("utf-8").split("x")[0], output.decode("utf-8").split("x")[1]
pygame_y = int(resolution_y) - 200.0
pygame_x = int(pygame_y) / 12.0 * 16.0



class Wombat:

    def __init__(self, img, x, y):
        self.img = img
        self.x = x * int(pygame_x / 16.0)
        self.y = y * int(pygame_y / 16.0)
        self.dir = 1
        self.leaves = 0
        self.leaf_img = pygame.transform.scale(pygame.image.load('leaf.png'), (int(pygame_x / 16.0)-2, int(pygame_y / 12.0)-2))
        self.broken = False


    def change_to_broken_image(self):
        broken_img = pygame.image.load('ball.png')
        broken_img = pygame.transform.scale(broken_img, (int(pygame_x / 16.0), int(pygame_y / 12.0)))
        self.img = broken_img
        self.world.display()


    def facing_north(self):
        if self.broken:
            return

        if self.dir == 0:
            return True
        else:
            return False


    def has_leaf(self):
        if self.broken:
            return

        if self.leaves > 0:
            return True
        else:
            return False


    def found_leaf_index(self):
        if self.broken:
            return
        
        for i, obj in enumerate(self.tile_objects):
            if obj.x == self.x and obj.y == self.y and isinstance(obj, Leaf):
                return i
        return -1
        

    def found_leaf(self):
        if self.broken:
            return
        
        for obj in self.tile_objects:
            if obj.x == self.x and obj.y == self.y and isinstance(obj, Leaf):
                return True
        return False


    def can_move(self):
        if self.broken:
            return

        for obj in self.tile_objects:
            if self.dir == 0:
                if self.x == obj.x and self.y-int(pygame_y / 12.0) == obj.y and isinstance(obj, Rock):
                    return False
            elif self.dir == 1:
                if self.x+int(pygame_x / 16.0) == obj.x and self.y == obj.y and isinstance(obj, Rock):
                    return False
            elif self.dir == 2:
                if self.x == obj.x and self.y+int(pygame_y / 12.0) == obj.y and isinstance(obj, Rock):
                    return False
            elif self.dir == 3:
                if self.x-int(pygame_x / 16.0) == obj.x and self.y == obj.y and isinstance(obj, Rock):
                    return False
        
        if self.x / int(pygame_x / 16.0) == 15 and self.dir == 1:
            return False
        elif self.x / int(pygame_x / 16.0) == 0 and self.dir == 3:
            return False
        elif self.y / int(pygame_y / 12.0) == 11 and self.dir == 2:
            return False
        elif self.y / int(pygame_y / 12.0) == 0 and self.dir == 0:
            return False
        else:
            return True


    def pick_leaf(self):
        if self.broken:
            return

        leaf_index = -1
        leaf_index = self.found_leaf_index()
        if not leaf_index == -1:
            self.tile_objects[leaf_index].num -= 1
            if self.tile_objects[leaf_index].num == 0:
                del self.tile_objects[leaf_index]
        else:
            self.broken = True
            self.change_to_broken_image()
            print("broken, tried to pick non existant leaf")
        self.world.display()


    def place_leaf(self):
        if self.broken:
            return
        
        in_tile_list = False
        if self.has_leaf():
            for obj in self.tile_objects:
                if obj.x == self.x and obj.y == self.y:
                    obj.num += 1
                    in_tile_list = True
                    
            if not in_tile_list:
                self.tile_objects.append(Leaf(self.leaf_img, int(self.x/int(pygame_x / 16.0)), int(self.y/int(pygame_y / 12.0)), 1))
        else:
            self.broken = True
            self.change_to_broken_image()
            print("broke, tried to place leaf even though didn't have any")


    def walk(self):
        if self.broken:
            return

        if not self.can_move():
            self.broken = True
            print("broken, hit edge or rock")
            self.change_to_broken_image()
        else:
            if self.dir == 0:
                self.y -= int(pygame_y / 12.0)
            elif self.dir == 1:
                self.x += int(pygame_x / 16.0)
            elif self.dir == 2:
                self.y += int(pygame_y / 12.0)
            elif self.dir == 3:
                self.x -= int(pygame_x / 16.0)
        self.world.display()


    def turn_left(self):
        if self.broken:
            return

        if self.dir == 0:
            self.dir = 3
        else:
            self.dir -= 1

        self.img = pygame.transform.rotate(self.img, 90)
        self.world.display()
        


    