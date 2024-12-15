The Rock-Paper-Scissors game is a classic hand game played between two players. Each player simultaneously forms one of three shapes: Rock, Paper, or Scissors. The winner is determined based on the following rules:

Rock crushes Scissors
Scissors cuts Paper
Paper covers Rock
This implementation allows the game to be played in two modes:

Between a player and the computer.
Between two players.

Mode Selection
At the start of the game, the user is prompted to choose between two modes:

Single Player: The player competes against the computer.
Player vs Player: Two players compete against each other.

Single Player Mode
The player inputs their choice (Rock, Paper, or Scissors).
The computer randomly selects its move using Python's random module.
The winner of each round is determined based on the standard rules.
The game continues until either the player or the computer wins 3 rounds.
Scores are displayed after each round, and the winner is announced when a player reaches 3 wins.

Player vs Player Mode
Both players input their choices (Rock, Paper, or Scissors).
The winner of each round is determined based on the standard rules.
The game continues until one of the players wins 3 rounds.
Scores are displayed after each round, and the winner is announced when a player reaches 3 wins.

Input Validation
The game checks whether the player's input is valid (Rock, Paper, or Scissors).
If the input is invalid, the game prompts the player to re-enter their choice.
Invalid inputs are handled gracefully with error messages and retries.