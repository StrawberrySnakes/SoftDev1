
"""Dessa Shapiro"""
NAME_TO_TABLE = {'t': [[1,1,1],[0,1,0]], 
                 'T': [[1,1,1],[0,1,0],[0,1,0]], 
                 'z': [[1,1,0],[0,1,1]],
                 'c': [[1,1],[1,0],[1,1]],
                 'f': [[1,1],[1,0],[1,1], [1,0]],
                 'L': [[1,0,0],[1,1,1]],
                 'l':[[1,0], [1,1]]}
EMPTY_SPOT = '-'
BLOCKER_SPOT = 'o'

def matrix(M):
    return [[ M[col][row] for col in range(len(M))] for row in range(len(M[0]))]

def reverse_rows(M):
    return M[::-1]

def reverse_columns(M):
    return [M[row][::-1] for row in range(len(M)) ]

def help_message():
    print("- 'help' to display commands")
    print("- 'quit' to quit the game" )
    print("- 'a <piece name> <row> <col>' to add a piece to the board at the position ") 
    print("- 'r <piece name>' to remove a piece")
    
class Shape:
    __slots__ = ['__table', '__position'] 
    
    def __init__(self, table):
        self.__table = table
        self.__position = None        
    
    def get_table(self):
        return self.__table   

    def get_position(self):
        return self.__position  

    def __repr__(self):
        return str(self.__table)

    def __eq__(self, other):
        return self.__table == other.__table

    def __hash__(self):
        return hash(str(self.__table))

    def fit(self, board, position):
        row, col = position
        for r in range(len(self.__table)):
            for c in range(len(self.__table[0])):
                if (
                    0 <= row + r < len(board) and
                    0 <= col + c < len(board[0]) and
                    self.__table[r][c] == 1 and
                    board[row + r][col + c] != EMPTY_SPOT
                ):
                    return False
        return True

    def add(self, board, position, symbol):
        if self.fit(board, position):
            row, col = position
            for r in range(len(self.__table)):
                for c in range(len(self.__table[0])):
                    if self.__table[r][c] == 1:
                        board[row + r][col + c] = symbol
            self.__position = position

    def remove(self, board):
        if self.__position:
            row, col = self.__position
            for r in range(len(self.__table)):
                for c in range(len(self.__table[0])):
                    if self.__table[r][c] == 1:
                        board[row + r][col + c] = EMPTY_SPOT
            self.__position = None

class Piece:
    __slots__ = ['__name', '__shapes', '__current_shape', '__fit_shapes_index']

    def __init__(self, name):
        self.__name = name
        self.__shapes = []
        self.__current_shape = None
        self.__fit_shapes_index = 0

    def get_name(self):
        return self.__name

    def get_current_shape(self):
        return self.__current_shape

    def get_fit_shapes(self):
        return self.__shapes

    def get_fit_shape(self):
        if self.__shapes:
            fit_shape = self.__shapes[self.__fit_shapes_index]
            self.__fit_shapes_index = (self.__fit_shapes_index + 1) % len(self.__shapes)
            return fit_shape
        return None


    
          
class Puzzle:
    __slots__ = ['__board', '__pieces', '__pieces_on_board', '__game_over']
    
    def __init__(self, blockers):
        self.__board = [[EMPTY_SPOT for _ in range(6)] for _ in range(6)]
        for r, c in blockers:
            self.__board[r][c] = BLOCKER_SPOT
               
    def play(self):
        print(self)
        while True:
            response = input("Enter a command or 'help': ")
            if response == "quit":
                print("Bye!")
                break
            elif response == "help":
                help_message()
            else:
                pass
    
    def __str__(self):
        s = '    0 1 2 3 4 5\n'
        s +='   ------------\n'
        for index in range(len(self.__board)):
            s += str(index) + " | "
            for elt in self.__board[index]:
                s += elt + " "
            s += "\n"
        return s
     
def main(): 
    # blocker_locations = ((0,1), (0,5), (2,0), (5,1), (5,4))
    # blocker_locations = ((0,0), (0,1), (3,4), (4,0), (5,5))
    blocker_locations = ((0,1), (0,3), (4,3), (5,3), (5,5)) 
    a_puzzle = Puzzle(blocker_locations)
    a_puzzle.play()
    
if __name__ == '__main__':     
    main()