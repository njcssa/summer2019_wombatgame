# wombatgame
A python port of a java programming game I used in AP CS

Made with [Pygame](https://github.com/pygame/pygame)

This is an updated version of [this repository](https://github.com/benjaminnow/wombatgame) and is going to be used in the NJCSSA's 2019 Introduction to Computer Programming class.

## Basic Info About The Wombat
- pretty much blind so has to count the steps it moves to keep track of where it is
- by default its only movements are walking one step in the direction it is facing and turning left (therefore to turn right it needs to make 3 left turns)
- can pick up leaves
- can drop leaves
- can check it is next to a wall or a rock
- will break if user's program instructs it to crash into a wall

## Basic info about the world
- the top left corner is [0, 0]
- the bottom right corner is [15, 11]
- each tile is about 50x50 pixels
- animation speed can be changed(in all the gifs it is 0.05 sec delay)
- an infinite loop can occur and will cause the program to freeze - in those cases, the program needs to be force quit

## Problems:

### Move until broken
![](/gifs/move_until_broken.gif)

### Move until can't
![](/gifs/move_until_cant.gif)

### Walk around the edge of the screen
![](/gifs/walk_edge.gif)

### Picking up only even stacks of leaves
![](/gifs/pick_only_evens.gif)

### Making a letter
![](/gifs/b.gif)

### Cleaning up whole grid
![](/gifs/world1.gif)

### Climbing over randomly generated mountains
![](/gifs/world10.gif)

### Making Screen-Saver animation
![](/gifs/screensaver.gif)

### Following coordinate list
coords list: # test coords list: [[1, 0], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [3, 5], [4, 5], [5, 5], [5, 6], [5, 7], [5, 8], [6, 8], [7, 8], [8, 8], [8, 9], [8, 10], [9, 10], [10, 10], [11, 10], [12, 10], [12, 11], [13, 11], [14, 11], [15, 11]]

![](/gifs/follow_coords.gif)

### Following waypoint coordinate list
coords list: [[5, 0], [10, 10], [4, 2], [15, 11]]

![](/gifs/follow_waypoint_coords.gif)

### Place leaves at specific coordinate locations
coords list: [[15, 11], [0, 0], [1, 1], [4, 3], [10, 7]]

![](/gifs/place_leaves_at_coords.gif)

### Making a checkered pattern
![](/gifs/checkered_pattern.gif)

### Climbing a small wall
![](/gifs/climb_small_wall.gif)

### Climbing a wall of random height
![](/gifs/climb_n_wall.gif)

### Making a rectangle with custom dimensions
2x2
![](/gifs/create_rect_2x2.gif)

3x5
![](/gifs/create_rect_3x5.gif)

### Making a spiral
![](/gifs/spiral.gif)

### Making a triangle with custom base size
9 base size
![](/gifs/triangle9.gif)

15 base size
![](/gifs/triangle15.gif)

### Wombat Bubble Sorts a row
![](/gifs/bubblesort.gif)

sorry, it takes a while

### Wombat Selection Sorts a row
![](/gifs/selectionsort.gif)

again, it takes a while


