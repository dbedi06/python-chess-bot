# AI Chess Bot
A fully functional chess engine powered by artificial intelligence, featuring the Minimax algorithm with Alpha-Beta pruning for efficient strategic gameplay.

## Project Overview
This project implements a complete chess game engine from scratch in Python, with an AI opponent that uses classical game theory algorithms to make intelligent moves. The bot evaluates positions by considering both material advantage and positional strength.

## Features
* Minimax Algorithm with Alpha-Beta Pruning: Efficient tree search that significantly reduces computation time while maintaining optimal play
* Custom Board Evaluation: Combining material count and piece-square tables for positional awareness
* Adjustable Difficulty Levels: Three AI difficulty settings (Easy, Medium, Hard) controlled by search depth
* Multiple Game Modes:
  * Human (White) vs AI (Black)
  * AI (White) vs Human (Black)
  * AI vs AI (spectator mode)
* Complete Chess Rules: Full move validation, check/checkmate detection, and legal move generation
* Modular Architecture: Clean, extensible codebase ready for future enhancements (GUI, opening books, etc.)
* Command-Line Interface: Simple, intuitive text-based gameplay

## Getting Started
### Prerequisites
* Python 3.8 or higher
* No external dependencies required. We only need the Python standard library

### Installation
1. Clone the repository:
```
git clone https://github.com/dbedi06/python-chess-bot.git
cd chess-ai-bot
```
2. Create and activate a virtual environment (could be redundant since the files are present, but still including it here):
```
python3 -m venv venv
Source venv/bin/activate # On Windows: venv/Scripts/activate
```
3. Run the game:
```
python main.py
```

## How to Play
1. Select Game Mode: Choose whether you want to play as White, Black, or watch two AIs play
2. Choose Difficulty:
  * Easy (depth 2): Around 200-500 nodes evaluated per move
  * Medium (depth 3): Around 5000-15000 nodes evaluated per move
  * Hard (depth 4): Around 20000-50000+ nodes evaluated per move
3. Make Moves: Enter moves in this notation, "e2e4" (to move from e2 to e4)
4. Special Commands:
  * "help": Displays the available legal moves
  * "quit": Exit the game (Warning: The game will insult you for backing out)

### Example Gameplay
```
a b c d e f g h
8|♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ |8
7|♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ |7
6|. . . . . . . . |6
5|. . . . . . . . |5
4|. . . . . . . . |4
3|. . . . . . . . |3
2|♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ |2
1|♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ |1
  ---------------
  a b c d e f g h

Move 1 - WHITE's turn
Your move (white):
```

## Project Structure
```
python-chess-bot/
│
├── main.py              # Entry point and command-line interface
├── chess_engine.py      # Core game logic and board management
├── ai_player.py         # Minimax algorithm with Alpha-Beta pruning
├── board_evaluator.py   # Position evaluation
├── piece.py             # Chess piece classes and move validation
├── move.py              # Move representation and notation conversion
└── README.md            # Project documentation (the file you are currently reading)
```

## Technical Implementation
### Minimax with Alpha-Beta Pruning
The AI uses a recursive Minimax algorithm to search the game tree, evaluating positions several moves ahead. Alpha-Beta pruning dramatically reduces the search space by eliminating branches that cannot influence the final decision.

Time Complexity: O(b^d) where b is the branching factor (around 35 for chess) and d is the search depth
Space Complexity: O(d) due to the recursive call stack

### Board Evaluation Function
The evaluation function scores positions based on:
1. Material Count: Standard piece values (Pawn = 100, Knight = 320, Bishop = 330, Rook = 500, Queen = 900)
2. Piece-Square Tables: Positional bonuses/penalties for each piece type based on board location
3. King Safety: Encourages castling and king protection in the opening/middlegame

### Performance Optimization
* Move Ordering: Captures are evaluated first to maximize Alpha-Beta cutoffs
* Deep Copying: Efficient board state duplication for tree search
* Early Termination: Alpha-Beta pruning reduces nodes evaluated by nearly 50-70%

## Algorithm Performance
| Difficulty | Search Depth | Avg. Nodes Evaluated | Avg. Time per Move |
|------------|--------------|----------------------|--------------------|
| Easy       | 2            | 200-500              | <0.1s              |
| Medium     | 3            | 5000-15000           | 0.5-2s             |
| Hard       | 4            | 20000-50000+         | 2-10s              |

Performance varies based on position complexity and the number of legal moves available

## Future Enhancements
Potential improvements for future versions:
  * Graphical User Interface: PyGame or Tkinter-based visual board
  * Opening Book: Database of common opening sequences
  * Transposition Tables: Cache evaluated positions to avoid redundant calculations
  * Iterative Deepening: Dynamic depth adjustment based on time constraints
  * Neural Network Integration: Machine learning-based evaluation function
  * UCI Protocol Support: Compatibility with chess GUIs like Arena or ChessBase

## Learning Outcomes
This project demonstrates:
  * Implementation of classical AI game-playing algorithms
  * Recursive problem-solving and tree search techniques
  * Object-oriented design and modular architecture
  * Performance optimization through algorithmic improvements
  * Complex rule validation and state management

## License
This project is open source

## Contributing
Contributions, issues, and feature requests are always welcome! Feel free to check the issues page.

## Acknowledgements
  * Chess piece symbols: Unicode chess characters
  * Algorithm inspiration: Claude Shannon's seminal 1950 paper on computer chess
  * Piece-square tables adapted from the Chess Programming Wiki
