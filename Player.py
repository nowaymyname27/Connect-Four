
from Board import Board

# write your class below.

class Player:
    '''Player class to represent a player of the Connect Four game.
    '''
    
    def __init__(self, checker):
        '''Constructs a new Player object by
        '''
        assert checker == 'X' or checker == 'O'
        
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        '''Returns a string representing a Player object.
        '''
        s = 'Player ' + self.checker
        
        return s
    
    def opponent_checker(self):
        '''Returns a one-character string representing the checker 
           of the Player object’s opponent.
        '''
        if self.checker == 'X':
            opponent = 'O'
        else:
            opponent = 'X'
        
        return opponent

    
    def next_move(self, b):
        '''Accepts a Board object b as a parameter and returns the column 
           where the player wants to make the next move.
        '''
        self.num_moves += 1
        
        while True:
            col = int(input('Enter a column: '))
            if col < b.width and col >= 0:
                return col
            else:
                print('Try again!')
        
        
    

    