# Connect Four

## Introduction

Connect Four is a classic two-player game where the objective is to get four of your colored checkers in a line, either horizontally, vertically, or diagonally. This game is played on a vertical grid of 6x7, with players taking turns to drop their checker in one of the seven columns. The game ends when either a player has made a line of four or all spaces on the board are filled and no such line was made (resulting in a tie).

This implementation of Connect Four in Python allows players to compete against each other, or against an artificial intelligence (AI) opponent. The AI uses a lookahead strategy, where it considers multiple future moves before deciding on its next move. 

## Installation

To install the game, clone the repository to your local machine and run it with Python 3.

```bash
git clone https://github.com/yourusername/connect-four.git
cd connect-four
python game.py
```

## How to play

After running the game, you will be prompted to choose the type of game you want to play: human vs. human, human vs. AI, or AI vs. AI.

For human players, you will be asked to input the column number (0 to 6) where you want to drop your checker. Make sure to strategize and block your opponent while working towards getting four of your own checkers in a line.

For AI players, you will be asked to specify a lookahead value and a tiebreak strategy ('LEFT', 'RIGHT', or 'RANDOM'). The lookahead value determines how many moves into the future the AI will consider before making a decision, and the tiebreak strategy is used when the AI has multiple equally good moves to choose from.

## How to play

After running the game, you can play the game using one of the three provided functions:

1. `play_game(tiebreaker, lookahead)`: This function initializes and plays a connect four game between a human player and an AI player. 

    - `tiebreaker` is a string that specifies the tiebreaking strategy for the AI player. It should be 'LEFT', 'RIGHT', or 'RANDOM'.
    
    - `lookahead` is an integer that determines the number of moves into the future the AI will consider before making a decision. It should be a non-negative integer.

2. `play_game2(lookahead)`: This function initializes and plays a connect four game between a human player and an AI player. In this version, the AI player uses a fixed 'LEFT' tiebreaking strategy. 

    - `lookahead` is an integer that determines the number of moves into the future the AI will consider before making a decision. It should be a non-negative integer.

3. `play_game3()`: This function initializes and plays a connect four game between a human player and an AI player. In this version, the AI player uses a fixed 'LEFT' tiebreaking strategy and a fixed lookahead of 4 moves.

For human players, you will be asked to input the column number (0 to 6) where you want to drop your checker. Make sure to strategize and block your opponent while working towards getting four of your own checkers in a line.

For AI players, you will specify a lookahead value and a tiebreak strategy while calling the respective function. The lookahead value determines how many moves into the future the AI will consider before making a decision, and the tiebreak strategy is used when the AI has multiple equally good moves to choose from.

## Strategies

1. For human players, the key is to stay one step ahead of your opponent. Always be on the lookout for opportunities to complete a line of four, and don't forget to block your opponent's attempts to do the same.

2. For AI players, the lookahead value and tiebreak strategy can significantly influence the outcome of the game. A higher lookahead value will make the AI more strategic but can slow down the game due to the increased computation. The tiebreak strategy can tip the balance in closely matched games.

Enjoy the game, and may the best player win!

## Strategies

1. For human players, the key is to stay one step ahead of your opponent. Always be on the lookout for opportunities to complete a line of four, and don't forget to block your opponent's attempts to do the same.

2. For AI players, the lookahead value and tiebreak strategy can significantly influence the outcome of the game. A higher lookahead value will make the AI more strategic but can slow down the game due to the increased computation. The tiebreak strategy can tip the balance in closely matched games.

Enjoy the game, and may the best player win!

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
