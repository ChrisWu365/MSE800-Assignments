'''
Activity Week 10-3: Develop a Tic-tac-toe Game Using Python
Develop a code decomposition and enhance your coding style. Once completed, share the GitHub link. (Estimated development time: 20 minutes)

Architecture Design:
1. main(): Entry of the game
2. create_board(): Create a board for the game
3. choose_player(): Choose to be O or X pleyer
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
            player_input = input(f'Please choose your game role(enter "O" or "X"), "O" will play first: ').upper()
            if self.is_choosen_player_correct(player_input):
                print(f'Invalid game role')
        self.human_player = player_input
        print(f'You have chosen {player_input}!')

    def play_in_turn(self):
        if self.human_player == self.current_player:
            try:
                grid_selected = input(f"({self.current_player}) Please enter your the grid number(1 to 9): ")
                int(grid_selected)
            except ValueError:
                return 
        print()

    def start_playing(self):
        """Take turns to play, "O" will play first"""
        self.current_player = "O"
        while True:
            # Play once and then take turns to play
            self.play_in_turn()
        print()
    def print_result():
        print(f"The winner is:")

    def main(self):
        self.create_board()
        self.choose_player()
        self.start_playing()
        self.print_result()

if __name__ == "__main__":
        tic_tac_toe = TicTacToe()
        tic_tac_toe.main()