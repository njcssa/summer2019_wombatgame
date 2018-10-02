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


########################################################################################################################
# ideas
# - wombat move until can't
# - wombat make a walk around the edge of the screen
# - make wombat make a checkered pattern on the screen with leaves
# - take coord inputs in a list and place leaves in those spots using function we made to go to any coord


########################################################################################################################
# wombat spiral inwards to center of screen


########################################################################################################################
# this will have the wombat go over a hill with 1 width


########################################################################################################################
# this will have the wombat place leaves in increasing bunches with them touching until the wombat can't move anymore
# from the starting position. The movement will be determined by randint.





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
             
        
#######################################################################################################################
    # bob.walk(), bob.turn_left(), bob.can_move(), bob.facing_north()
    
    # def turn_right(self):
    #     bob.turn_left()
    #     bob.turn_left()
    #     bob.turn_left()

    # def turn_left_x_times(self, x):
    #     pass

    def walk_x_times(self, x):
        for i in range(0, x):
            bob.walk()

    # def turn_x_dir(self, x):
    #     while not bob.facing_north():
    #         bob.turn_left()

    #     if x == 3:
    #         bob.turn_left()
    #     elif x == 2:
    #         bob.turn_left()
    #         bob.turn_left()
    #     elif x == 1:
    #         bob.turn_left()
    #         bob.turn_left()
    #         bob.turn_left()

    # def make_x_big_square(self, x):
    #     bear = 0
    #     while bear < 4:
    #         self.walk_x_times(x-1)
    #         bob.turn_left()
    #         bear += 1

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


    def goto_x_y(self, x, y):
        self.turn_x_dir(2)
        while bob.can_move():
            bob.walk()
        self.turn_x_dir(3)
        while bob.can_move():
            bob.walk()
        self.turn_x_dir(1)
        for i in range(x):
            bob.walk()
        self.turn_x_dir(0)
        for k in range(y):
            bob.walk()



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


    



    def screen_saver2(self):
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
                pass

        
        

    def run(self):
        #self.screen_saver()
        self.walk_place_diagonally(3, 1)
        self.walk_place_diagonally(3, 0)
        