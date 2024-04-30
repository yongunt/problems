def is_win(var:str, board:list) -> bool:
    win:bool = None
    # rows
    for i in range(len(board)):
        win = True
        for j in range(len(board)):
            if board[i][j] != var:
                win = False
                break

    if win: return win
    # columns
    for i in range(len(board)):
        win = True
        for j in range(len(board)):
            if board[j][i] != var:
                win = False
                break

    if win: return win
    # diagonals
    for i in range(len(board)):
        win = True
        if board[i][i] != var:
            win = False
            break

    if win: return win

    for i in range(len(board)):
        win = True
        if board[i][len(board) - 1 - i] != var:
            win = False
            break

    return win


def tic_tac_toe(board:list) -> str:
    if is_win(var='X', board=board): return "Player 1 Wins"
    elif is_win(var='O', board=board): return "Player 2 Wins"
    else: return "It's a Tie"


print(tic_tac_toe([
  ["X", "O", "O"],
  ["O", "X", "O"],
  ["O", "#", "X"]
]))

print(tic_tac_toe([
  ["X", "O", "O"],
  ["O", "X", "O"],
  ["X", "#", "O"]
]))

print(tic_tac_toe([
  ["X", "X", "O"],
  ["O", "X", "O"],
  ["X", "O", "#"]
]))


'''
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
'''