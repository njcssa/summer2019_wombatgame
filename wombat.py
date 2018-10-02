import pygame
from pygame.locals import *
from leaf import Leaf
from rock import Rock


class Wombat:

    def __init__(self, img, x, y):
        self.img = img
        self.x = x * 50
        self.y = y * 50
        self.dir = 1
        self.leaves = 0
        self.leaf_img = pygame.transform.scale(pygame.image.load('leaf.png'), (48, 48))
        self.broken = False


    def change_to_broken_image(self):
        broken_img = pygame.image.load('ball.png')
        broken_img = pygame.transform.scale(broken_img, (50, 50))
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
                if self.x == obj.x and self.y-50 == obj.y and isinstance(obj, Rock):
                    return False
            elif self.dir == 1:
                if self.x+50 == obj.x and self.y == obj.y and isinstance(obj, Rock):
                    return False
            elif self.dir == 2:
                if self.x == obj.x and self.y+50 == obj.y and isinstance(obj, Rock):
                    return False
            elif self.dir == 3:
                if self.x-50 == obj.x and self.y == obj.y and isinstance(obj, Rock):
                    return False
        
        if self.x / 50 == 15 and self.dir == 1:
            return False
        elif self.x / 50 == 0 and self.dir == 3:
            return False
        elif self.y / 50 == 11 and self.dir == 2:
            return False
        elif self.y / 50 == 0 and self.dir == 0:
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
                self.tile_objects.append(Leaf(self.leaf_img, self.x/50, self.y/50, 1))
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
                self.y -= 50
            elif self.dir == 1:
                self.x += 50
            elif self.dir == 2:
                self.y += 50
            elif self.dir == 3:
                self.x -= 50
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
        


    