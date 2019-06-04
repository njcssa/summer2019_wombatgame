import pygame
from pygame.locals import *
from time import sleep
from random import randint
from leaf import Leaf
from rock import Rock

class World:
    def __init__(self, size, wombat, screen, delay, setup):
        self.size = size #tuple (width, height)
        self.wombat = wombat
        self.screen = screen
        self.delay = delay
        self.leaf_img = pygame.transform.scale(pygame.image.load('leaf.png'), (48, 48))
        self.rock_img = pygame.transform.scale(pygame.image.load('rock.png'), (50, 50))
        self.tile_objects = []
        # setup 0 is a clean board
        if setup == 1:
            self.random_leaves()
        elif setup == 2:
            self.random_leaves()
            self.random_rocks()
        elif setup == 3:
            self.one_wall()
        elif setup == 4:
            self.maze()
        elif setup == 10:
            self.mountains()


    def get_grid_background(self):
        background = pygame.Surface(self.size)
        background = background.convert()
        background.fill((255, 221, 153))

        colnum = 16
        rownum = 12

        for i in range(0, colnum):
            for j in range(0, rownum):
                x = i * 50
                y = j * 50
                pygame.draw.rect(background, (0, 0, 0), (x, y, 50, 50), 1)

        background.blit(self.wombat.img, (self.wombat.x, self.wombat.y))

        return background


    def something_on_spot(self, x, y):
        for obj in self.tile_objects:
            if obj.x == x*50 and obj.y == y*50:
                return True
        return False


    def random_leaves(self):
        # used for setup 1 where wombat collects all the leaves on the board
        for i in range(0, 25):
            chosen_x_y = [randint(0, 15), randint(0, 11)]
            while (chosen_x_y[0]*50 == self.wombat.x and chosen_x_y[1]*50 == self.wombat.y) or self.something_on_spot(chosen_x_y[0], chosen_x_y[1]):
                chosen_x_y = [randint(0, 15), randint(0, 11)]
            leaf_image = Leaf(self.leaf_img, chosen_x_y[0], chosen_x_y[1], randint(1, 10))
            self.tile_objects.append(leaf_image)

    
    def random_rocks(self):
        for i in range(0, 10):
            chosen_x_y = [randint(0, 15), randint(0, 11)]
            while (chosen_x_y[0]*50 == self.wombat.x and chosen_x_y[1]*50 == self.wombat.y) or self.something_on_spot(chosen_x_y[0], chosen_x_y[1]):
                chosen_x_y = [randint(0, 15), randint(0, 11)]
            rock_image = Rock(self.rock_img, chosen_x_y[0], chosen_x_y[1])
            self.tile_objects.append(rock_image)


    def one_wall(self):
        x = randint(3, 12)
        y = 12
        height = randint(2, 9)
        for i in range(height):
            rock_image = Rock(self.rock_img, x, y)
            y -= 1
            self.tile_objects.append(rock_image)


    def maze(self):
        startx = 7
        starty = 5
        leaf_num = 1
        # 0-up, 1-right, 2-down, 3-left
        while (startx > 0 and startx < 15) and (starty > 0 and starty < 11):
            currentx = startx
            currenty = starty
            iterations = 0
            while self.something_on_spot(currentx, currenty):
                currentx = startx
                currenty = starty
                direction = randint(0, 3)
                if direction == 0:
                    currenty -= 1
                elif direction == 1:
                    currentx += 1
                elif direction == 2:
                    currenty += 1
                elif direction == 3:
                    currentx -= 1
                iterations += 1
                if iterations > 50:
                    break
            if iterations > 50:
                break
            # breaks used when random leaf placement is not possible(ex. surrounded on all sides)
            startx = currentx
            starty = currenty
            self.tile_objects.append(Leaf(self.leaf_img, startx, starty, leaf_num))
            leaf_num += 1



    def mountains(self):
        # need to setup wombat in main at the bottom left corner
        final_height = 0
        for i in range(4, 16):
            height = randint(0, 7)
            for j in range(0, height):
                new_rock = Rock(self.rock_img, i, 11-j)
                self.tile_objects.append(new_rock)
            if i == 15:
                final_height = height
        self.tile_objects.append(Leaf(self.leaf_img, i, 11-final_height, 1))


    def display_tile_objects(self):
        grid_background = self.get_grid_background()
        for obj in self.tile_objects:
            grid_background.blit(obj.get_image(), (obj.x+1, obj.y+1))

        return grid_background


    def display(self):
        pygame.event.get()
        background = self.display_tile_objects()

        self.screen.blit(background, (0, 0))
        pygame.display.flip()
        sleep(self.delay)