# Define the transition function
# Modified from 'turn functionality commit'
import traceback
import sys

class Board(object):
    
    def __init__(self, list2d, cursor_at='O'):
        """Initializes the board with whose turn. Default is `O`"""
        self.board = list2d
        self.playerO = 'O'
        self.playerX = 'X'
        self.cursor_at = cursor_at
        self.game_over = False        

    def is_game_over(self):
        return self.game_over

    def get_turn(self):
        return self.cursor_at

    def get_current_state(self):
        return self.board

    def is_valid(self, src, dst):
        """Checking to see if it's possible to move from src to dst.
        Position is indicated by a tuple of the form (row, column).
        NB: It works only when the `O` player moves UP and `X` moves
        down"""

        try:
            (x,y) = src
            (a,b) = dst
            srcSym = self.get_sym(src)
            dstSym = self.get_sym(dst)
            
            # CP1(CheckPoint1): Invalid Index, negative and outside of list
            if None in [srcSym, dstSym]:
                # print("Out of bound error, both negative and larger than size")
                return False

            # CP2: source /= destination, same row movement not permitted either
            if x == a:
                # print("Error: src=dst")
                return False
            
            # CP3: Wrong Move Direction    
            # For player `O`, the valid dest direction is upwards
            if srcSym == self.playerO:
                if x == (a + 1):
                    pass
                else:
                    # print("The direction is not upward")
                    return False
            # For `X` the valid dest direction is downwards
            if srcSym == self.playerX:
                if x == (a - 1):
                    pass
                else:
                    # print("The direction is not downward")
                    return False

            # CP4: Movement of more than one unit
            # The jump cannot be more than one unit forward or diagonal
            col_diff = abs(y - b)
            if col_diff > 1 or col_diff < 0:
                return False
            
            # CP5: Occupied by the same player
            # A move can be made when the dst is either `.` or enemy
            if dstSym == srcSym:
                return False
            else:
                return True

        except IndexError as e:
            # print ("out of the board {0} {1}".format(dst, e))
            return False


    def display_state(self):
        """Prints out the state passed to this function on the terminal.""" 
        print("\n######################################################\n")
        for row in self.board:
            for column in row:
                print(column, end=' ')
            print("\n")
        
        print("######################################################\n")
        return
   

    def get_sym(self, position):
        """Returns the symbol/character at position passed. 
           Returns None if it's neither `O` nor `X`"""
        try:
            (x, y) = position
     
            # Negative indices DOES NOT raise indexError in Python
            # Board contains only positive (x,y) values.
            for i in position:
                if i < 0:
                    return None
            sym = self.board[x][y].upper()
            if sym == self.playerO:
                return 'O' # or self.playerO
            elif sym == self.playerX:
                return 'X'
            elif sym == '.':
                return '.'
            else:
                return None
        except IndexError:
            return None


    def get_direction(self, posit):
        """To get upwards or downwards direction for a given position"""
        try:
            sym = self.get_sym(posit)
            direction = None
            if sym == 'O':
                direction = 'U'
            elif sym == 'X':
                direction = 'D'
            else:
                direction = None
            return direction
        
        except Exception:
            return None


    def get_positions(self, player):
        """Returns all the position occupied by a certain player"""
        try:
            if player not in [self.playerX, self.playerO]:
                # print("Incorrect marker passed for player's symbol.")
                raise ValueError
                traceback.print_stack(file=sys.stdout)

            positions_found = []
            for x, row in enumerate(self.board):
                for y, column in enumerate(row):
                    if column == player:
                        positions_found.append((x,y))
            
            return positions_found

        except Exception as e:
            print("Exception occurred: ", e)
            traceback.print_stack(file=sys.stdout)

    def all_moves(self, player):
        """Returns a data structure full of possible moves by a player"""
        
        all_positions = self.get_positions(player)
        movement_dict = {}
    
        for position in all_positions:
            # A single source
            (x,y) = position
            # Is this moving upwards or downwards
            flow = self.get_direction(position)
            # All the moves for this position in a list
            moves_for_this_position = self.get_moves(position)
        
            for i, move in enumerate(moves_for_this_position):
                (x1, y1) = move
                if flow == 'U':
                    if y1 == y + 1:      # to the right
                        # Replacing the destination with letter
                        moves_for_this_position[i] = 'R'
                    elif y1 == y - 1:      # to the left
                        # Replacing the destination with letter
                        moves_for_this_position[i] = 'L' 
                    elif y1 == y:      # to forward
                        # Replacing the destination with letter
                        moves_for_this_position[i] = 'F'
                    else:
                        print("Somethig wrong in the get_moves function")

                elif flow == 'D':
                    if y1 == y - 1:      # to the right
                        # Replacing the destination with letter
                        moves_for_this_position[i] = 'R'
                    elif y1 == y + 1:      # to the left
                        # Replacing the destination with letter
                        moves_for_this_position[i] = 'L' 
                    elif y1 == y:      # to forward
                        # Replacing the destination with letter
                        moves_for_this_position[i] = 'F'
                    else:
                        print("Sth wrong in the get_moves function")
                else:
                    print("Direction is neither up nor down. Invalid")

            movement_dict[position] = moves_for_this_position

        return movement_dict


    def get_moves(self, posit):
        """Returns a list of valid moves for the position passed"""
        try:
            (x,y) = posit
            direction = self.get_direction(posit)
            all_moves = []
            valid_moves = []
            if direction == 'U':
                # direction upwards, (x-1, y-1): diagonal left,
                # (x-1, y): forward, (x-1, y+1): diagonal right
                all_moves = [(x-1, y-1), (x-1, y), (x-1,y+1)]
            elif direction == 'D':
                # direction upwards, (x+1, y-1): diagonal left,
                # (x+1, y): forward, (x+1, y+1): diagonal right
                all_moves = [(x+1, y-1), (x+1, y), (x+1,y+1)]
            
            elif direction == '.':
                pass
            else:
                # last elif and this else can be combined
                pass

            # Filtering the valid moves
            for move in all_moves:
                if self.is_valid(posit, move) == True:
                    valid_moves.append(move)
                else:
                    pass
            return valid_moves
        except TypeError:
            print("Invalid position, TypeError raised.")
            return []

    
    def terminal_state(self):
        """Check if current state is a terminal one."""
        # Need to change the variable names to make things more consistent
        player1 = False
        player2 = False

        p1list = []
        p2list = []

        for row in self.board:
            for element in row:
        #First case, when one of the players pieces is all out
                if element is self.playerX:
                    p1list.append(element)
                if element is self.playerO:
                    p2list.append(element)

        #Second case, when one of the pieces move to the last row
        for element in self.board[-1]:
            if element == "X":
                player1 = True
        for element in self.board[0]:
            if element == "O":
                player2 = True

        #Print the result for both cases 
        if player1 is True:
            # print("First case, when one of the players pieces is all out")
            #print("Game Over. Player X won")
            self.game_over = True
            return self.playerX
        if player2 is True:
            # print("First case, when one of the players pieces is all out")
            #print("Game Over. Player O won")
            self.game_over = True
            return self.playerO

        if len(p1list) == 0:
            # print ("Second case, when one of the pieces move to the last row")
            #print("Game Over. Player O won")
            self.game_over = True
            return self.playerO
        if len(p2list) == 0:
            # print ("Second case, when one of the pieces move to the last row")
            #print("Game Over. Player X won")
            self.game_over = True
            return self.playerX
        
        # None of the winning conditions returned True
        return None
 

    def switch_turn(self):
        if self.cursor_at == self.playerO:
            self.cursor_at = self.playerX
        elif self.cursor_at == self.playerX:
            self.cursor_at = self.playerO
        else:
            raise Exception

        return self.cursor_at
            

    def move(self, posit, turn):
        """Move to the direction =['R','L','F'] asked to from position passed"""
        try:
            # Check if it's current players turn
            if self.cursor_at != self.get_sym(posit):
                # print("Move not allowed. {0}'s turn now".format(self.cursor_at))
                return False

            # Identify the destination
            (x, y) = posit
            # Initialize the destination tuple
            a = 99999999
            b = 99999999
            flow = self.get_direction(posit)
            # Figuring out the dest X (=a) value
            if flow == 'U':
                a = x - 1                
                # Figuring out the dest Y (=b) value
                if turn == 'R':
                    b = y + 1
                elif turn == 'L':
                    b = y - 1
                elif turn == 'F':
                    b = y
                else:
                    print ("Invalid move direction")
                    return False
            elif flow == 'D':
                a = x + 1

                if turn == 'R':
                    b = y - 1
                elif turn == 'L':
                    b = y + 1
                elif turn == 'F':
                    b = y
                else:
                    print ("Invalid move direction")
                    return False

            else:       
                # When get_direction == None, return Failure
                return False
            
            # validate move
            dest = (a,b)
            if self.is_valid(posit, dest) != True:
                return False
            
            # Move the current player to the dest, assign `.` at empty spot
            self.board[a][b] = self.board[x][y]
            self.board[x][y] = '.'
            
            # Flip the turn to the other player
            # print("{0} just played.".format(self.cursor_at))
            self.switch_turn()
            # print("Next is {0}'s turn.".format(self.cursor_at))
            return True

        except Exception as e:
            # Anything goes wrong
            print("Exception occured: ", e)
            return False
            
