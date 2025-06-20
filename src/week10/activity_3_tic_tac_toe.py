'''
Activity Week 10-3: Develop a Tic-tac-toe Game Using Python
Develop a code decomposition and enhance your coding style. Once completed, share the GitHub link. (Estimated development time: 20 minutes)

Architecture Design:
1. main(): Entry of the game
2. create_board(): Create a board for the game
3. choose_player(): Choose to be O or X player
4. start_playing(): Start playing the game
5. print_result(): Print game result
'''
PLAYER_SET = {"O", "X"}

class TicTacToe:
    def __init__(self):
        self.board = None
        self.human_player = None
        self.current_player = None

    def create_board(self):
        self.board = [["-" for _ in range(3)] for _ in range(3)]

    def is_choosen_player_correct(self, player_input):
        return player_input not in PLAYER_SET

    def choose_player(self):
        player_input = None
        while self.is_choosen_player_correct(player_input):
            player_input = input(f'Please choose your game role (enter "O" or "X"), "O" will play first: ').upper()
            if self.is_choosen_player_correct(player_input):
                print(f'Invalid game role')
        self.human_player = player_input
        print(f'You have chosen {player_input}!')

    def display_board(self):
        for row in self.board:
            print(" | ".join(row))
        print()

    def is_valid_move(self, grid_selected):
        try:
            grid_selected = int(grid_selected)
            if grid_selected < 1 or grid_selected > 9:
                return False
            # Calculate row and col once
            self.row, self.col = divmod(grid_selected - 1, 3)
            return self.board[self.row][self.col] == "-"
        except ValueError:
            return False

    def make_move(self):
        # Use pre-calculated row and col
        self.board[self.row][self.col] = self.current_player

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != "-":
                print("check rows for winner")
                return row[0]
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "-":
                print("check columns for winner")
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "-":
            print("check diagonals1 for winner")
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "-":
            print("check diagonals2 for winner")
            return self.board[0][2]

        return None

    def is_draw(self):
        return all(cell != "-" for row in self.board for cell in row)

    def play_in_turn(self):
        self.display_board()
        if self.human_player == self.current_player:
            # human player input
            while True:
                grid_selected = input(f"Player ({self.current_player}) Please enter your grid number (1 to 9): ")
                if self.is_valid_move(grid_selected):
                    self.make_move()
                    break
                print("Invalid move. Please try again.")
        else:
            # computer player input
            print(f"Computer player ({self.current_player}) : ")
            for i in range(1, 10):
                if self.is_valid_move(i):
                    self.make_move()
                    break
        self.current_player = "O" if self.current_player == "X" else "X"

    def start_playing(self):
        """Take turns to play, "O" will play first"""
        self.current_player = "O"
        while True:
            self.play_in_turn()
            winner = self.check_winner()
            if winner:
                self.display_board()
                print(f"The winner is: {winner}")
                break
            if self.is_draw():
                self.display_board()
                print("The game is a draw!")
                break

    def main(self):
        self.create_board()
        self.choose_player()
        self.start_playing()

if __name__ == "__main__":
    tic_tac_toe = TicTacToe()
    tic_tac_toe.main()