"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    previous = 0    #the last compared nonzero value
    merge_list = []   #the merge list
    for tile in line:
        if tile == previous and previous !=0: #merges
            previous = 0
            merge_list.pop()
            merge_list.append(tile*2)
        elif tile != 0:
            previous = tile
            merge_list.append(tile)
    return merge_list + [0 for element in range(len(line)-len(merge_list))]

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height #Height and Width
        self._grid_width = grid_width
        self._cells = []
        key_up = [(0, sub_up) for sub_up in range(grid_width)]
        key_down = [(grid_height-1, sub_down) for sub_down in range(grid_width)]
        key_right = [(sub_right, grid_width-1) for sub_right in range(grid_height)]
        key_left = [(sub_left, 0) for sub_left in range(grid_height)]
        self.direction = {UP: key_up, DOWN: key_down, LEFT: key_left, RIGHT: key_right}
        #Creates initial board
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._cells = [ [0 for sub_col in range(self._grid_width)] for sub_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return ' '.join(''.join(str(sub_tile) for sub_tile in sub_row) for sub_row in self._cells)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        index_list = self.direction[direction]
        line_range = {UP: range(self._grid_height), DOWN: range(self._grid_height),
                        LEFT: range(self._grid_width), RIGHT: range(self._grid_width)}
        new_add = 0
        for index in index_list:
            temporary = []
            for num in line_range[direction]:   # Retrieve line
                row = OFFSETS[direction][0]*num + index[0]
                col = OFFSETS[direction][1]*num + index[1]
                temporary += [ self._cells[row][col] ]
            temporary = merge(temporary)        # Merge the line
            for num in line_range[direction]:   # Store the merged tile values back into the grid
                row = OFFSETS[direction][0]*num + index[0]
                col = OFFSETS[direction][1]*num + index[1]
                if self._cells[row][col] != temporary[num]:
                    new_add =1                
                self._cells[row][col] = temporary[num]
        if new_add == 1:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        empty = [] # Empty Grid (Row and Column)
        random_tile = [2 for sub_x in range(9)] + [4]
        for sub_i, row in enumerate(self._cells):   # Find empty square
            for sub_j, tile in enumerate(row):
                if tile == 0: 
                    empty += [(sub_i, sub_j)]
        row, col = random.choice(empty)        # Random grid selection
        self._cells[row][col] = random.choice(random_tile)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._cells[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._cells[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))