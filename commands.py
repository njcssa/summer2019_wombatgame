#####################################################################################################################################################################
# ideas
# - wombat move until can't
# - wombat make a walk around the edge of the screen
# - make wombat make a checkered pattern on the screen with leaves
# - take coord inputs in a list and place leaves in those spots using function we made to go to any coord
# - wombat spiral inwards with leaves in increasing numbers to center of screen from edge
# - make wombat go over hill with height of 1 rock
# - make wombat create rectangle of certain dimensions
# - make wombat create pyramid/triangle of certain base width



#####################################################################################################################################################################



import time
class Commands:
    def __init__(self, wombat):
        self.wombat = wombat
        global bob
        bob = self.wombat # change name to whatever you want
        bob.leaves = 1000


######################################################################################################################################################################
# little helper functions developed in class

    def turn_right(self):
        bob.turn_left()
        bob.turn_left()
        bob.turn_left()

    def pick_all_leaves_on_spot(self):
        while bob.found_leaf():
            bob.pick_leaf()

    def place_x_leaves(self, num):
        for i in range(0, num):
            if bob.has_leaf():
                bob.place_leaf()

    def turn_north(self):
        while not bob.facing_north():
            bob.turn_left()

    def turn_x_dir(self, num):
        self.turn_north()

        i = 4
        while i > num:
            bob.turn_left()
            i -= 1

    def leaves_on_spot(self):
        leaves = 0
        i = 0
        while bob.found_leaf():
            bob.pick_leaf()
            leaves += 1
        while i < leaves:
            bob.place_leaf()
            i += 1

      #return leaves

    def walk_x_times(self, x):
        for i in range(0, x):
            bob.walk()


    def walk_and_place(self, x):
        for i in range(0, x):
            bob.place_leaf()
            bob.walk()

    def walk_place_diagonally(self, x, dir):
        for i in range(0, x):
            bob.place_leaf()
            if dir == 1:
                self.turn_x_dir(1)
                bob.walk()
                self.turn_x_dir(0)
                bob.walk()
            elif dir == 2:
                self.turn_x_dir(2)
                bob.walk()
                self.turn_x_dir(1)
                bob.walk()
            elif dir == 3:
                self.turn_x_dir(3)
                bob.walk()
                self.turn_x_dir(2)
                bob.walk()
            elif dir == 0:
                self.turn_x_dir(0)
                bob.walk()
                self.turn_x_dir(3)
                bob.walk()


########################################################################################################################
# wombat moves until he can't anymore

    # this will show how wombat can hurt itself if it runs into a wall
    def move_until_broken(self):
        i = 0
        while i < 20:
            bob.walk()
            i += 1


    def move_until_cant(self):
        while bob.can_move():
            bob.walk()


########################################################################################################################
# walk around edge of screen - assumes wombat starts in top left corner
# each function shows gradual improvement - uses functions made before

    def walk_edge_1(self):
        while bob.can_move():
            bob.walk()
        self.turn_right()
        while bob.can_move():
            bob.walk()
        self.turn_right()
        while bob.can_move():
            bob.walk()
        self.turn_right()
        while bob.can_move():
            bob.walk()
        self.turn_right()

    def walk_edge_2(self):
        i = 0
        while i < 4:
            while bob.can_move():
                bob.walk()
            self.turn_right()
            i += 1

    def walk_edge_3(self):
        for i in range(0, 4):
            self.move_until_cant()
            self.turn_right()
########################################################################################################################
# pick up all leaves in row which have an even number and leave piles with odd numbers
# use world setup 5

    def pick_even_leaves(self):
        amount_on_spot = 0
        while bob.can_move():
            while bob.found_leaf():
                bob.pick_leaf()
                amount_on_spot += 1
            if not amount_on_spot % 2 == 0:
                for i in range(amount_on_spot):
                    bob.place_leaf()
            amount_on_spot = 0
            bob.walk()

########################################################################################################################
# wombat makes a checkered pattern on the screen
# assumes starting in top left corner

    def make_checkered_row(self):
        steps = 0
        while bob.can_move():
            if steps % 2 == 0:
                bob.place_leaf()
            bob.walk()
            steps += 1

    def make_checkered_pattern(self):
        rows = 0
        while rows < 12:
            self.make_checkered_row()
            self.turn_x_dir(2)
            if rows < 11: # add this later after students see problem with code - makes it so wombat doesn't hit wall on last row
                bob.walk()
            if rows % 2 == 0:
                self.turn_x_dir(3)
            else:
                self.turn_x_dir(1)
            rows += 1

########################################################################################################################
# make wombat place leaves at specific coordinate locations
# test coordinate list: [[15, 11], [0, 0], [1, 1], [4, 3], [10, 7]]

    # explain that wombat is pretty blind and can only detect where walls are - therefore he has to go to walls to orient himself and
    # he cannot tell what space he is on - that's why this function is useful
    def goto_x_y(self, x, y):
        self.turn_x_dir(3)
        while bob.can_move():
            bob.walk()
        self.turn_x_dir(0)
        while bob.can_move():
            bob.walk()
        self.turn_x_dir(1)
        for i in range(x):
            bob.walk()
        self.turn_x_dir(2)
        for k in range(y):
            bob.walk()

    def place_leaves_at_coords(self, coords):
        for i in range(0, len(coords)):
            self.goto_x_y(coords[i][0], coords[i][1])
            bob.place_leaf()

########################################################################################################################
# make wombat create a spiral of leaves inwards

    def one_loop(self, xsize, ysize, num_leaf):
        for i in range(2):
            for i in range(xsize-1):
                self.place_x_leaves(num_leaf)
                bob.walk()
            self.turn_right()
            for i in range(ysize-1):
                self.place_x_leaves(num_leaf)
                bob.walk()
            self.turn_right()
        self.turn_x_dir(1)
        bob.walk()
        self.turn_x_dir(2)
        bob.walk()
        self.turn_x_dir(1)

    def spiral(self):
        xsize = 16
        ysize = 12
        leaf_amount = 1
        while ysize > 1:
            self.one_loop(xsize, ysize, leaf_amount)
            xsize -= 2
            ysize -= 2
            leaf_amount += 1
            

########################################################################################################################
# wombat climbs over a 1 tall mountain
# need to use setup 6
# start wombat in lower left corner

        
    def climb_over_hill(self):
        self.move_until_cant()
        self.turn_x_dir(0)
        bob.walk()
        self.turn_x_dir(1)
        self.walk_x_times(2)
        self.turn_x_dir(2)
        bob.walk()
        self.turn_x_dir(1)
        self.move_until_cant()

########################################################################################################################
# wombat climbs over random height mountain
# need to use specific world setup for this problem
# start wombat in lower left corner


    def climb_over_n_wall(self):
        self.move_until_cant()
        while not bob.can_move():
            self.turn_x_dir(0)
            bob.walk()
            self.turn_x_dir(1)
        self.walk_x_times(2)
        self.turn_x_dir(2)
        self.move_until_cant()
        self.turn_x_dir(1)
        self.move_until_cant()



########################################################################################################################
# create rectangle of certain dimensions
# start wombat in upper left corner

    def create_rectangle(self, xsize, ysize):
        for i in range(ysize):
            if i % 2 == 0:
                for j in range(xsize):
                    bob.place_leaf()
                    bob.walk()
            else:
                while bob.can_move():
                    bob.place_leaf()
                    bob.walk()
                bob.place_leaf()
            self.turn_x_dir(2)
            bob.walk()
            if i % 2 == 0:
                self.turn_x_dir(3)
                bob.walk()
            else:
                self.turn_x_dir(1)


########################################################################################################################
# create triangle of certain base width
# start wombat in upper left corner

    def calculate_num_rows(self, basesize):
        rows = 0
        while basesize >= 1:
            rows += 1
            basesize -= 2
        return rows

    def make_triangle(self, basesize):
        self.turn_x_dir(2)
        num_rows = self.calculate_num_rows(basesize)
        self.walk_x_times(num_rows)
        self.turn_x_dir(1)
        current_row = 0
        while basesize >= 1:
            if current_row % 2 == 0:
                self.walk_and_place(basesize)
                self.turn_x_dir(0)
                bob.walk()
                self.turn_x_dir(3)
                self.walk_x_times(2)
                basesize -= 2
                current_row += 1
            else:
                self.walk_and_place(basesize)
                self.turn_x_dir(0)
                bob.walk()
                self.turn_x_dir(1)
                self.walk_x_times(2)
                basesize -= 2
                current_row += 1

########################################################################################################################
# make wombat follow a list of coordinates on a path and place leaf on every square
# assumes wombat starts in top left corner
# test coords list: [[1, 0], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [3, 5], [4, 5], [5, 5], [5, 6], [5, 7], [5, 8], [6, 8], [7, 8], [8, 8], [8, 9], [8, 10], [9, 10], [10, 10], [11, 10], [12, 10], [12, 11], [13, 11], [14, 11], [15, 11]]
    
    def follow_coordinates(self, coords_list):
        startx = 0
        starty = 0
        bob.place_leaf()
        for i in range(len(coords_list)):
            if coords_list[i][0] > startx:
                self.turn_x_dir(1)
                bob.walk()
                startx += 1
            elif coords_list[i][0] < startx:
                self.turn_x_dir(3)
                bob.walk()
                startx -= 1
            elif coords_list[i][1] > starty:
                self.turn_x_dir(2)
                bob.walk()
                starty += 1
            elif coords_list[i][1] < starty:
                self.turn_x_dir(0)
                bob.walk()
                starty -= 1
            bob.place_leaf()
    

########################################################################################################################
# make wombat follow a path of coordinates which has gaps in it
# assumes wombat starts in top left corner
# test coords: [[5, 0], [10, 10], [4, 2], [15, 11]]

    def follow_waypoint_coords(self, coords_list):
        startx = 0
        starty = 0
        for i in range(len(coords_list)):
            dx = coords_list[i][0] - startx
            dy = coords_list[i][1] - starty

            if dx > 0:
                self.turn_x_dir(1)
                self.walk_and_place(dx)
            elif dx < 0:
                self.turn_x_dir(3)
                self.walk_and_place(-1*dx)
            
            if dy > 0:
                self.turn_x_dir(2)
                self.walk_and_place(dy)
            elif dy < 0:
                self.turn_x_dir(0)
                self.walk_and_place(-1*dy)
            
            startx = coords_list[i][0]
            starty = coords_list[i][1]


########################################################################################################################

# gets wombat to clean up all of the random leaves on the board

    def setup_1_solution(self):
        i = 1
        while i < 13:
            while bob.can_move():
                self.pick_all_leaves_on_spot()
                bob.walk()
            if not i % 2 == 0 and not i == 12:
                self.turn_right()
                self.pick_all_leaves_on_spot() # get leaves on turning spot
                bob.walk()
                self.turn_right()
            elif not i == 12:
                bob.turn_left()
                self.pick_all_leaves_on_spot()
                bob.walk()
                bob.turn_left()
            i += 1
            self.pick_all_leaves_on_spot() # accounts for last spot


#######################################################################################################################
# mountains solution
# wombat needs to have 0 leaves to start and go in the bottom right corner


    def rock_below(self):
        self.turn_x_dir(2)
        if bob.can_move():
            self.turn_x_dir(1)
            return False
        else:
            self.turn_x_dir(1)
            return True

    def finding_first_hill(self):
        while bob.can_move():
            bob.walk()

    def going_up(self):
        print("going up")
        
        while not bob.can_move():
            self.turn_x_dir(0)
            bob.walk()
            self.turn_x_dir(1)
        while self.rock_below():
            bob.walk()

    def going_sideways(self):
        print("going sideways")
        bob.walk()
        if bob.found_leaf():
            bob.pick_leaf()
        while self.rock_below() and bob.can_move():
            bob.walk()
        if bob.found_leaf():
            bob.pick_leaf()

    def at_peak(self):
        counter = 0
        self.turn_x_dir(3)
        if bob.can_move():
            counter += 1
        self.turn_x_dir(2)
        if bob.can_move():
            counter += 1
        self.turn_x_dir(1)
        if counter == 2 or bob.x == 50 * 15:
            return True
        else:
            return False
        

    def get_to_peak(self):
        print("going to peak")
        while not self.at_peak():
            self.going_up()
            self.going_sideways()


    def surrounded_except_top(self):
        counter = 0
        self.turn_x_dir(1)
        if not bob.can_move():
            counter += 1
        self.turn_x_dir(2)
        if not bob.can_move():
            counter += 1
        self.turn_x_dir(3)
        if not bob.can_move():
            counter += 1

        self.turn_x_dir(1)
        if counter == 3:
            return True
        else:
            return False


    def keep_going_down(self):
        counter = 0
        self.turn_x_dir(3)
        if not bob.can_move():
            counter += 1
        self.turn_x_dir(2)
        if not bob.can_move():
            counter += 1

        self.turn_x_dir(1)
        if counter == 2:
            return True
        else:
            return False



    def going_down(self):
        print("going down")
        self.turn_x_dir(2)
        while bob.can_move():
            bob.walk()
        if bob.found_leaf():
            bob.pick_leaf()
        
        
        
    
    def setup_10_solution(self):
        self.finding_first_hill()
        while bob.x / 50 < 15:
            print("first")
            self.get_to_peak()
            self.going_down()
            while self.keep_going_down() and not self.surrounded_except_top():
                print("second")
                self.going_sideways()
                self.going_down()
            self.turn_x_dir(1)
            print("end")
             
        
################################################################################################################################
# makes the letter B out of leaves

    def make_b(self):
        self.turn_x_dir(0)
        for i in range(0, 11):
            bob.place_leaf()
            bob.walk()
        self.turn_right()
        self.walk_and_place(4)
        self.turn_right()
        bob.walk()
        self.walk_and_place(3)
        bob.place_leaf()
        bob.walk()
        self.turn_right()
        bob.walk()
        self.walk_and_place(3)
        self.turn_x_dir(2)
        bob.walk()
        self.turn_x_dir(1)
        bob.walk()
        bob.walk()
        bob.walk()
        bob.walk()
        bob.place_leaf()
        self.turn_x_dir(2)
        bob.walk()
        self.turn_x_dir(1)
        bob.walk()
        bob.place_leaf()
        self.turn_x_dir(2)
        bob.walk()
        self.walk_and_place(3)
        self.turn_x_dir(3)
        bob.walk()
        self.walk_and_place(4)
        
##############################################################################################################################################
# eats all the leaves on the screen by going row to row

    def row(self):
        while bob.can_move():
            while not bob.found_leaf() and bob.can_move():
                bob.walk()
            while bob.found_leaf():
                bob.pick_leaf()

    
    def eat_everything(self):
        for i in range(1, 13):
            if i % 2 == 1:
                self.row()
                self.turn_right()
                bob.walk()
                self.turn_right()
            elif i % 2 == 0:
                self.row()
                if i != 12:
                    bob.turn_left()
                    bob.walk()
                    bob.turn_left()

############################################################################################################################################
# bouncing ball effect with placing leaves
# breaks when in corner


    def screen_saver(self):
        direction = 1
        while bob.has_leaf():
            self.walk_place_diagonally(1, direction)
            if direction == 1:
                self.turn_x_dir(0)
                if not bob.can_move():
                    direction = 2
                self.turn_x_dir(1)
                if not bob.can_move():
                    direction = 0
            elif direction == 2:
                self.turn_x_dir(1)
                if not bob.can_move():
                    direction = 3
                self.turn_x_dir(2)
                if not bob.can_move():
                    direction = 1
            elif direction == 3:
                self.turn_x_dir(2)
                if not bob.can_move():
                    direction = 0
                self.turn_x_dir(3)
                if not bob.can_move():
                    direction = 2
            elif direction == 0:
                self.turn_x_dir(3)
                if not bob.can_move():
                    direction = 1
                self.turn_x_dir(0)
                if not bob.can_move():
                    direction = 3


###################################################################################################################################################################  
        

    def run(self):
        time.sleep(3)
        self.place_leaves_at_coords([[15, 11], [0, 0], [1, 1], [4, 3], [10, 7]])
        #pass
        