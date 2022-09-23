
from rps import rock_paper_scissors
from wordle import Wordle
from connectfour import ConnectFour
from tictactoe import TicTacToe
while True:
    txt = """Mini Games!!!
    - Rock, Paper, Scissors (1)
    - Wordle (2)
    - ConnectFour (3)
    - Tic Tac Toe (4)
Select a game (press a number or 'q' to quit): """
    value = input(txt)

    if value == "1":
        rock_paper_scissors()
        # TODO: check against all possible cases, "Rock smashes scissors"
    elif value == "2":
        game = Wordle()
        game.play()
        # TODO: load wordlist from file
    elif value == "3":
        game = ConnectFour()
        game.play()
        # TODO: make this colorful, use colored token
    elif value == "4":
        game = TicTacToe()
        game.play()
        # TODO: random start, make computer more intelligent
    elif value == "q":
        break