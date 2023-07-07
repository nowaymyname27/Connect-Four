
from Board import Board
from Player import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b
        
def process_move(p, b):
    '''Takes two parameters: a Player object p for the player whose move 
       is being processed, and a Board object b for the board on which the game is being played.
    '''
    print("Player", p.checker + "'s", 'turn', '\n')
    
    p_move = p.next_move(b)
    
    b.add_checker(p.checker, p_move)
    
    print()
    print(b)
    
    win_lose = b.is_win_for(p.checker)
    tie = b.is_full()
    
    if win_lose == True:
        print('Player', p.checker, 'wins in', p.num_moves, 'moves.')
        print('Congratulations!')
        return True
    elif tie == True:
        print("It's a tie!")
        return True
    else:
        return False
    
    
class RandomPlayer(Player):
    """
    Represents a random player in the game, which is a subclass of the Player class.
    This player chooses a random valid move for each turn.
    """

    def next_move(self, b):
        """
        Determines the next move for the RandomPlayer by selecting a random column
        in the board (b) that can still accommodate a piece. Updates the number
        of moves made by the player.
        """
        self.num_moves += 1
    
        available_columns = []
        for col in range(b.width):
            if b.can_add_to(col):
                available_columns += [col]
    
        return random.choice(available_columns)



    
    
    
    
    
    
    
    