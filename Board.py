
class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    
    def __init__(self, height, width):
        '''constructs a new Board object
        '''
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        s += '-' + '-' * (self.width * 2) + '\n'
        
        for col in range(self.width):
            if col < 10:
                s += ' ' + str(col)
            else:
                s += ' ' + str(col % 10)
        
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        row = self.height - 1
        while row >= 0:
            if self.slots[row][col] == ' ':
                self.slots[row][col] = checker
                return
            row -= 1
    
    ### add your reset method here ###
    
    def reset(self):
        '''reset the Board object on which it is called by 
           setting all slots to contain a space character.
        '''
        self.slots = [[' '] * self.width for row in range(self.height)]
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    
    def can_add_to(self, col):
        '''The can_add_to method checks if a piece can be added to the
           specified column of the game board represented by the current object.
        '''
        if col < 0 or col > (self.width-1):
            return False
        for row in range(self.height):
            if self.slots[row][col] == ' ':
                return True
        return False
    
    def is_full(self):
        '''The is_full method checks if the game board represented by 
           the current object is completely filled with pieces or not.
        '''
        for row in range(self.height):
            for col in range(self.width):
                if self.slots[row][col] == ' ':
                    return False
        return True
    
    def remove_checker(self, col):
        """Removes the top checker from the specified column of the game board 
          represented by the current object, or does nothing if the column is empty.
        """
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                return
            
    def is_win_for(self, checker):
        """
        Checks if the specified checker has won the game by having four checkers in a row, 
        column, or diagonal on the game board represented by the current object.
        """
        assert checker == 'X' or checker == 'O'
    
        for row in range(self.height):
            for col in range(self.width):
                if col <= self.width - 4:
                    # Check horizontal
                    if self.slots[row][col] == checker and \
                       self.slots[row][col+1] == checker and \
                       self.slots[row][col+2] == checker and \
                       self.slots[row][col+3] == checker:
                        return True
                if row <= self.height - 4:
                    # Check vertical
                    if self.slots[row][col] == checker and \
                       self.slots[row+1][col] == checker and \
                       self.slots[row+2][col] == checker and \
                       self.slots[row+3][col] == checker:
                        return True
                if row <= self.height - 4 and col <= self.width - 4:
                    # Check diagonal (top-left to bottom-right)
                    if self.slots[row][col] == checker and \
                       self.slots[row+1][col+1] == checker and \
                       self.slots[row+2][col+2] == checker and \
                       self.slots[row+3][col+3] == checker:
                        return True
                if row <= self.height - 4 and col >= 3:
                    # Check diagonal (top-right to bottom-left)
                    if self.slots[row][col] == checker and \
                       self.slots[row+1][col-1] == checker and \
                       self.slots[row+2][col-2] == checker and \
                       self.slots[row+3][col-3] == checker:
                        return True

        # if we make it here, there was no win
        return False


    
    
