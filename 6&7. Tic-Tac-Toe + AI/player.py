import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input Move 0-8: ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again!')

        return val

# TicTacToe AI
class GeniusCompuerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) # randomly choose one
        else:
            # get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {
                'position': None,
                'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
            }
        elif not state.empty_squares(): # no empty squares
            return {
                'position': None,
                'score': 0
            }

        if player == max_player:
            best = {'position': None, 'score': -math.inf} # each score should maximize (be larger)
        else:
            best = {'position': None, 'score': math.inf} # each score should minimize

        for possible_move in state.available_moves():
            # Step 1: Make a move, try that spot
            state.make_move(possible_move, player)
            # Step 2: recurse using minimax to stimulate a game after making that move
            sim_score = self.minimax(state, other_player) # now, we alternate players

            # Step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move # otherwise this will get messed up

            # Step 4: update the dictionaries if necessary
            if player == max_player: # we are trying to maximize the max_player
                if sim_score['score'] > best['score']:
                    best = sim_score # replace the best
            else: # but minimize the other player
                if sim_score['score'] < best['score']:
                    best = sim_score # replace the best

        return best