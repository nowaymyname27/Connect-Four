

import random  
from Game import *

class AIPlayer(Player):
    """
    Represents an AI player in the game, which is a subclass of the Player class.
    This player uses a lookahead strategy to choose its next move and takes
    advantage of inheritance from the Player class.
    """

    def __init__(self, checker, tiebreak, lookahead):
        """
        Initializes a new AIPlayer object with the given checker, tiebreak strategy, 
        and lookahead value.
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
        
    def __repr__(self):
        """
        Returns a string representation of the AIPlayer object, including the checker, 
        tiebreak strategy, and lookahead value.
        """
        s = 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        
        return s
    
    def max_score_column(self, scores):
        """
        Returns the index of the column with the maximum score, applying the AIPlayer's 
        tiebreaking strategy in case of a tie.
        """
        max_score = max(scores)
        max_indices = []
        
        for i in range(len(scores)):
            if scores[i] == max_score:
                max_indices += [i]
        
        if self.tiebreak == 'LEFT':
            return max_indices[0]
        elif self.tiebreak == 'RIGHT':
            return max_indices[-1]
        else:
            return random.choice(max_indices)
    
    def scores_for(self, b):
        """
        Determines the AIPlayer's scores for the columns in the given board and returns a 
        list containing one score for each column.
        """
        scores = [0] * b.width
    
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            else:
                b.add_checker(self.checker, col)
                if b.is_win_for(self.checker):
                    scores[col] = 100
                elif b.is_win_for(self.opponent_checker()):
                    scores[col] = 0
                elif self.lookahead == 0:
                    scores[col] = 50
                else:
                    opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                    opp_scores = opponent.scores_for(b)
                    scores[col] = 100 - max(opp_scores)
                b.remove_checker(col)
    
        return scores
    def next_move(self, b):
        """
        Determines and returns the AIPlayer's best possible move based on the 
        current board state.
        """
        scores = self.scores_for(b)
        best_move = self.max_score_column(scores)
        self.num_moves += 1
        
        return best_move

def play_game(tiebreaker, lookahead):
    """
    Initializes and plays a connect four game between a human player and an AI player.

    Args:
        tiebreaker (str): The tiebreaking strategy for the AI player. Should be 'LEFT', 'RIGHT', or 'RANDOM'.
        lookahead (int): The number of moves the AI player should look ahead. Should be a non-negative integer.

    Returns:
        None
    """
    p1 = Player('X')
    p2 = AIPlayer('O', tiebreaker, lookahead)

    connect_four(p1, p2)

def play_game2(lookahead):
    """
    Initializes and plays a connect four game between a human player and an AI player. 
    In this version, the AI player uses a fixed 'LEFT' tiebreaking strategy.

    Args:
        lookahead (int): The number of moves the AI player should look ahead. Should be a non-negative integer.

    Returns:
        None
    """
    p1 = Player('X')
    p2 = AIPlayer('O', 'LEFT', lookahead)

    connect_four(p1, p2)

def play_game3():
    """
    Initializes and plays a connect four game between a human player and an AI player. 
    In this version, the AI player uses a fixed 'LEFT' tiebreaking strategy and a fixed lookahead of 4 moves.

    Args:
        None

    Returns:
        None
    """
    p1 = Player('X')
    p2 = AIPlayer('O', 'LEFT', 4)

    connect_four(p1, p2)
