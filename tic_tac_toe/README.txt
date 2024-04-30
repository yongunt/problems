Tic Tac Toe
Create a function that takes a list of character inputs from a Tic Tac Toe game. Inputs will be taken from player1 as "X", player2 as "O", and empty spaces as "#". The program will return the winner or tie results.

Examples
tic_tac_toe([
  ["X", "O", "O"],
  ["O", "X", "O"],
  ["O", "#", "X"]
]) ➞ "Player 1 wins"


tic_tac_toe([
  ["X", "O", "O"],
  ["O", "X", "O"],
  ["X", "#", "O"]
]) ➞ "Player 2 wins"


tic_tac_toe([
  ["X", "X", "O"],
  ["O", "X", "O"],
  ["X", "O", "#"]
]) ➞ "It's a Tie"

source --> https://edabit.com/challenge/5Q2RRBNJ8KcjCkPwP