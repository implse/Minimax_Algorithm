# Minimax Algorithm

<p align="center">
  <img width="480" height="360" src="images\Minimax.png">
</p>

The minimax algorithm returns the best possible move for a given game state. It assumes that your opponent will also be using the minimax algorithm to determine their best move.

A game can be represented as a tree. The current state of the game is the root of the tree, and each potential move is a child of that node. The leaves of the tree are game states where the game has ended (either in a win or a tie).

Game states can be evaluated and given a specific score. This is relatively easy when the game is over — the score is usually a 1, -1 depending on who won. If the game is a tie, the score is usually a 0.
