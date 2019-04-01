"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100       # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board, player):
    """
    mc_trial checks the board and the next player to 
    be moved, makes random choice 
    and alternates the players
    """
    while not board.check_win(): #Checks that no one has won yet
        row, col = random.choice(board.get_empty_squares()) #Selects random tile
        board.move(row,col,player)
        player = provided.switch_player(player)
        
def mc_update_scores(scores, board, player):
    """
    Reviews the score, one of thr board from a completed 
    game and machine player.
    Scores completed board and update 
    """
    status = board.check_win() #Check status
    alternate_player = provided.switch_player(player)
    dimensions = board.get_dim()
    if status == player:
        score_current_t = SCORE_CURRENT
        score_other_t = SCORE_OTHER
    elif status == alternate_player:
        score_current_t = -SCORE_CURRENT
        score_other_t = -SCORE_OTHER
    else:
        return
    for dummy_row in range(dimensions):
        for dummy_col in range(dimensions):
            square = board.square(dummy_row, dummy_col)
            if square == player:
                scores[dummy_row][dummy_col] += score_current_t
            elif square == alternate_player:
                scores[dummy_row][dummy_col] -= score_other_t

def get_best_move(board, scores):
    """The function takes board and scores.
    It'll find the empty squares with the highest score
    and return it as a tuple"""
    empty_board = board.get_empty_squares() #Checks for empty squares
    max_score = float('-inf')
    max_score_position = [] #List will contain the max score positions
    for square in empty_board:
        row, col = square
        if scores[row][col] > max_score:
            max_score_position = [(row, col)]
            max_score = scores[row][col]
        elif scores[row][col] == max_score:
            max_score_position.append((row,col))
    return random.choice(max_score_position)

def mc_move(board, player, trials):
    """
    Function takes board and grid of scores.
    It will find the empty squares with tha max score and
    return one of them as a tuple
    """
    scores = [[0 for dummy_x in range(board.get_dim())] for dummy_x in range(board.get_dim())]
    for dummy_trial in range(trials):
        trial_board = board.clone()
        mc_trial(trial_board, player)
        mc_update_scores(scores, trial_board, player)
    return get_best_move(board, scores)

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
