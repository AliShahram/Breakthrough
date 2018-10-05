from transition import Board
from minmax import Minimax_Agent

class Agent(object):
    """An agent receives a board state, i.e., a 2-d list as input at moment 
    And makes a decision based on that, and sends the next move back to the
    game controlling identity"""

    def __init__(self, current_state, turn,  utility_func, symbol):
        """Agent is initiated with a utility function associated with"""
        self.utility = utility_func
        self.state = current_state
        self.turn = turn
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol

    def update_state(self, new_state):
        """Update the state with the one passed."""
        try:
            self.state = new_state
            return True
        except Exception as e:
            print("Error updating Agent's state: {}".format(e))
            return False

    def next_move(self, current_state, turn):
        """Use the minimax tree and the utility function to figure out the next
        move.

        rtype: a tuple, a string (in that order)
        """
        # Initialize a minimax tree.
        decisionTree = Minimax_Agent(current_state, turn, self.utility)
        decisions = decisionTree.get_val()
        dest = decisions[0]        
        move_direction = decisions[1]

        return dest, move_direction
