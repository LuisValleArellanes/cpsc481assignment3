board = [" " for _ in range(9)]

def display_board():
    for row in range(3):
        print("|".join(board[row*3:row*3+3]))
        if row < 2:
            print("-----")
            
def player_move(symbol):
    while True:
        move = input(f"{symbol}, enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == " ":
            board[int(move) - 1] = symbol
            break
        else:
            print("Invalid move. Try again.")

def tic_tac_toe_win(board, symbol):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(all(board[pos] == symbol for pos in condition) for condition in win_conditions)

def tic_tac_toe_tie(board):
    return " " not in board

def minimax(board, depth, is_maximizing, symbol):
  if symbol == "O":
    opponent == "X"
  else:
   symbol == "X"

  if tic_tac_toe_win(board, symbol ):
    return -1
  if tic_tac_toe_win(board, opponent ):
    return 1
  if tic_tac_toe_tie(board):
    return 0 
  if is_maximizing:
    max_eval = int ('-inf')
    for i in range (9)
      if board[i] == "":
        board[i] = symbol



def get_player_choice():
    while True:
        choice = input("Do you want to be 'O' or 'X'? ").upper()
        if choice in ["O", "X"]:
            return choice

if __name__ == "__main__":
    player_symbol = get_player_choice()
    ai_symbol = "O" if player_symbol == "X" else "X"
    current_symbol = "O"  # O starts first

    while True:
        display_board()
        if current_symbol == player_symbol:
            player_move(player_symbol)
        else:
            #AI MOVE

        if check_win(board, current_symbol):
            display_board()
            if current_symbol == player_symbol:
                print("Congratulations, you win!")
            else:
                print("AI wins!")
            break
        elif check_tie(board):
            display_board()
            print("It's a tie!")
            break

        current_symbol = ai_symbol if current_symbol == player_symbol else player_symbol
