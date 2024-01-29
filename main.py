import os
import sys
import chess

def display_board(board):
    print(board)

def get_move(board):
    fen = board.fen()
    print(f"Current position ({len(list(board.legal_moves))} legal moves):")
    print(fen)
    move = input("Enter your move (e.g. e2e4): ").lower()
    try:
        move = chess.Move.from_uci(move)
        if move in board.legal_moves:
            return move
        else:
            print("Illegal move. Try again.")
            return get_move(board)
    except ValueError:
        print("Invalid input. Try again.")
        return get_move(board)

def main():
    board = chess.Board()
    while not board.is_game_over():
        os.system('cls' if os.name == 'nt' else 'clear')
        display_board(board)
        move = get_move(board)
        board.push(move)
    print("Game over.")
    print(board.result())

if __name__ == "__main__":
    main()