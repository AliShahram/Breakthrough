from agent import Agent
from utilities import *
from transition import Board
from tools import initial_state

def setup_game():
    print("Welcome to Breakthrough!")
    print("This game has 4 different intelligent agents you can play with.")
    print("Please choose the opponent agents")

    agents = { 1: 'Evasive',
            2: 'Conquerer',
            3: 'House Lannister',
            4: 'House Stark'
            }
    for i in range(1,5):
        print("{0} : {1}".format(i, agents[i]))

    try:
        print("Enter two numbers between 1 and 4, separated by a space:")
        agent1, agent2 = map(int, input().split())
        agent1 = int(agent1)
        agent2 = int(agent2)
        print("You have chosen {0} and {1} to play".format(agents[agent1],
                                                        agents[agent2]))

        utility_functions = {1: evasive,
                            2: conqueror,
                            3: house_lannister,
                            4: house_stark
                            }        

        print("\nPlease decide how your board should look like.")
        print("Enter # of rows, # of columns and # of rows with players")
        print("separated by spaces")
        row, col, p_rows = map(int, input().split())
        if p_rows > row:
            raise ValueError("rows with players must be less than # of rows")       
 
        list2d = initial_state(row, col, p_rows)
        print("This is how the board looks like:")

        print("\n######################################################\n")
        for row in list2d:
            for column in row:
                print(column, end= " ") 
            print("\n")        
        print("######################################################\n")

    except (KeyError,ValueError) as e:
        print("KeyError or ValueError occured: ", e)
        print("Please try again.")

    return list2d, utility_functions[agent1], utility_functions[agent2]

def run_game(list2d, agent1, agent2):
    """This is where the game runs.
    The agents interact with the Board here
    The Board make sure to enforce the game rules."""

    Smith = 'X'
    John = 'O'
    starting_turn = Smith
    agent_smith = Agent(list2d, starting_turn, agent1, Smith)
    agent_john = Agent(list2d, starting_turn, agent2, John)

    # initialize the Board
    board = Board(list2d, John)
    print("Player {0} has the first turn".format(starting_turn))

    moves = 0
    while True:
        moves = moves + 1
        # retrieve the current state
        curr = board.get_current_state()
        # show the current state
        board.display_state()
        whose_turn = board.get_turn()
        
        next_move = None
        if whose_turn == Smith:
            print("{0}'s turn now.".format(Smith))
            next_move = agent_smith.next_move(curr, Smith)
        elif whose_turn == John:
            next_move = agent_john.next_move(curr, John) 
            print("{0}'s turn now.".format(John))
        else:
            print("Something wrong with the board")
      
 
        move_dest, direction = next_move    
        # Perform the move on the board
        # Try again if it's wrong turn

        move_success = board.move(move_dest, direction)
        if move_success == True:
            # Keep playing
            board.display_state()
            pass
        else:
            print("Try a valid move.")

        # print(board.terminal_state())
        if board.terminal_state() != None: 
            print("This game Ended. To play again, run `game.py`")
            break
        # show the new state
    print("Total number of moves made:", moves)

if __name__ == '__main__':
    list2d, player1, player2 = setup_game()
    run_game(list2d, player1, player2)
