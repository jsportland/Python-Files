# tic.py
# Jeff Smith
# Basic Tic-Tac-Toe game

# Set the board
import os
os.system('clear')


class Board():
    def __init__(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def drawBoard(self):
        print(' %c | %c | %c' % (self.board[1], self.board[2], self.board[3]))
        print('-----------')
        print(' %c | %c | %c' % (self.board[4], self.board[5], self.board[6]))
        print('-----------')
        print(' %c | %c | %c' % (self.board[7], self.board[8], self.board[9]))

    def update_cell(self, cell_num, player):
        if self.board[cell_num] == ' ':
            self.board[cell_num] = player
        else:
            return "That move is not allowed"

    def winner(self, player):
        row1 = [self.board[1], self.board[2], self.board[3]]
        row2 = [self.board[4], self.board[5], self.board[6]]
        row3 = [self.board[7], self.board[8], self.board[9]]
        col1 = [self.board[1], self.board[4], self.board[7]]
        col2 = [self.board[2], self.board[5], self.board[8]]
        col3 = [self.board[3], self.board[6], self.board[9]]
        diag1 = [self.board[1], self.board[5], self.board[9]]
        diag2 = [self.board[3], self.board[5], self.board[7]]
        for comb in (row1, row2, row3, col1, col2, col3, diag1, diag2):
            if comb == [player, player, player]:
                return True
            if comb == [player, player, player]:
                return True
            return False

    def tie_board(self):
        full_cell = 0
        for cell in self.board:
            if cell != ' ':
                full_cell += 1
        if full_cell == 9:
            return True
        else:
            return False

    def play_again(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


b1 = Board()


class Player():
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __repr__(self):
        return f"({self.token}): {self.name}"


name_list = []
token_list = ['X', 'O']

player_name = input("Who will play 'X'?: ").lower()
name_list.append(player_name)
player2_name = input("Who will play 'O'?: ").lower()
name_list.append(player2_name)

for num in range(2):
    c1 = Player(name=name_list[num], token=token_list[num])


# Game functions
def introduction():
    print('Let\'s Play Tic Tac Toe!')


def start_game():
    # Display board
    b1.drawBoard()


    # Run the game
while True:
    start_game()
    introduction()

    # Get input for player x
    x_input = int(
        input(f'\nX: {name_list[0]}) Please choose a cell to place your token. 1 - 9: '))
    # Update the cell they chose
    b1.update_cell(x_input, 'X')
    start_game()
    introduction()
    # Check for x win
    if b1.winner('X'):
        print('Hooray! X wins!')
        play_again = input(
            'Would you like to play again? Please enter "y" for yes and "n" for no: ').lower()
        if play_again == 'y':
            b1.play_again()
            continue
        else:
            break
    # Check for a tie
    if b1.tie_board():
        print('The game is a tie!')
        play_again = input(
            'Would you like to play again? Please enter "y" for yes and "n" for no: ').lower()
        if play_again == 'y':
            b1.play_again()
            continue
        else:
            break
    # Get input for player O
    o_input = int(
        input(f'\nO: {name_list[1]}) Please choose a cell to place your token. 1 - 9: '))

    # Update the cell they chose to populate thier token
    b1.update_cell(o_input, 'O')
    # Check for an O win
    if b1.winner('O'):
        print('Hooray! O wins!')
        play_again = input(
            'Would you like to play again? Please enter "y" for yes and "n" for no: ').lower()
        if play_again == 'y':
            b1.play_again()
            continue
        else:
            break
    # Check for a tie
    if b1.tie_board():
        print('The game is a tie!')
        play_again = input(
            'Would you like to play again? Please enter "y" for yes and "n" for no: ').lower()
        if play_again == 'y':
            b1.play_again()
            continue
        else:
            break
# End
