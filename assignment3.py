board = [" " for _ in range(9)]

def display_board(board):
    for row in range(3):
        print("|".join(board[row*3:row*3+3]))
        if row < 2:
            print("-----")
    print ("\n")
def player_move(board, symbol):
    while True:
        move = input(f"PLayer {symbol}, enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == " ":
            board[int(move) - 1] = symbol
            break
        else:
            print("Invalid move. Try again.")

def check_win(board, symbol):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), 
                      (0,3,6), (1,4,7), (2,5,8),
                      (0,4,8), (2,4,6)]
    for conditions in win_conditions:
        if board[win_conditions[0]] == board[win_conditions[1]] == board[win_conditions[2]] == symbol:
            return True
    return any(all(board[pos] == symbol for pos in condition) for condition in win_conditions)

def check_tie(board):
    return " " not in board

def minimax(board, depth, is_maximizing, ai_symbol, human_symbol, symbol):
  if check_win(board, ai_symbol):
      return 1
  elif check_win(board, human_symbol):
      return -1
  elif check_tie(board):
      return 0 

  if is_maximizing:
    max_eval = int ('-inf')
    for i in range (9):
      if board[i] == "":
        board[i] = symbol
        eval = minimax(board, depth + 1, False, symbol)
        board[i] = " "
        max_eval = max(max_eval, eval)
    return max_eval    
  else:
      min_eval = int('inf')
      for i in range (9):
        if board[i] == " ":
          board[i] = human_symbol
          eval = minimax(board, depth + 1, True,ai_symbol, human_symbol)
          board[i] = " "
          min_eval = min(min_eval, eval)
      return min_eval



def get_player_choice():
    while True:
        choice = input("Do you want to be 'O' or 'X'? ").upper()
        if choice in ["O", "X"]:
            return choice

def best_move(board, ai_symbol, human_symbol):
    best_score = -float('inf')
    move = -1
    for i in range(len(board)):
        if board[i] == " ":
            board[i] = ai_symbol
            score = minimax(board, 0, False, ai_symbol, human_symbol, ai_symbol)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

if __name__ == "__main__":
    player_symbol = get_player_choice()
    ai_symbol = "O" if player_symbol == "X" else "X"
    current_symbol = "O"  # O starts first
    board = [" " for _ in range(9)]
    
    while True:
        display_board(board)
        if current_symbol == player_symbol:
            player_move(board, player_symbol)
        else:
            #AI MOVE
            display_board(board)
            if current_symbol == player_symbol:
                player_move(board, player_symbol)
            else:
                move = best_move(board, ai_symbol, player_symbol)
                if move == -1:
                    print("NO MOVES LEFT")
                    break
            board[move] = ai_symbol
            print(f"AI places {ai_symbol} in postion {move+1}")
            display_board(board)
            
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
