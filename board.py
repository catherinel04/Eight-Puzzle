#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Catherine Liu
# email:cliu26@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Fiona Wu
# partner's email: fionayw@bu.edu
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(3):
            for c in range(3):
                digit = digitstr[3*r + c]
                self.tiles[r][c] = digit
                if digit == '0':
                    self.blank_r = r
                    self.blank_c = c

    ### Add your other method definitions below. ###
    def __repr__(self):
        """ returns a string representation of a Board object """
        s = ''
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '0':
                    s += '_ '
                else:
                    s += self.tiles[r][c] + ' '
            s += '\n'
        return s
                
    def move_blank(self, direction):
        """ Attempts to modify the contents of the called 
            Board object accordingly
            input direction: specifies the direction in which 
            the blank should move
        """
        if direction not in 'up down left right':
            return False
        else:
            
            for r in range(3):
                for c in range(3):
                    if self.tiles[r][c] == '0':
                        row = r
                        col = c
                        if direction == 'up':
                            row -= 1
                        elif direction == 'down':
                            row += 1
                        elif direction == 'left':
                            col -= 1
                        elif direction == 'right':
                            col += 1

                        if (row < 0 or row > 2) or (col < 0 or col > 2):
                            return False
                        else:
                            self.tiles[r][c] = self.tiles[row][col]
                            self.tiles[row][col] = '0'
                            self.blank_r = row
                            self.blank_c = col
                            return True
    
    def digit_string(self):
        """ returns a string of digits that corresponds to current contents of
            called Board object's tiles attribute"""
        s = ''
        for r in range(3):
            for c in range(3):
                s += str(self.tiles[r][c])
        return s
    
    def copy(self):
       """ returns a deep copy of new board object """
       copy_tiles = Board(self.digit_string())
       return copy_tiles
       
    def num_misplaced(self):
         """ counts and returns the number of tiled in the called Board object 
             that are not where they should be in goal state"""
         count = 0
         for r in range(3):
             for c in range(3):
                 if self.tiles[r][c] in '12345678':
                     if GOAL_TILES[r][c] != self.tiles[r][c]:
                         count +=1
         return count     

    def __eq__(self, other):
        """ compare two Board objects """
        if self.tiles == other.tiles:
            return True
        else:
            return False
        
    
    def num_wrong(self):
        """ calculated and returns how many tiles are in wrong row and column """
        count = 0
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] in '12345678':
                    if self.tiles[r][c] not in GOAL_TILES[r]:
                        count += 1
                    if int(self.tiles[r][c]) % 3 != c:
                        count += 1
        return count
                    
                
            
                
                
    
