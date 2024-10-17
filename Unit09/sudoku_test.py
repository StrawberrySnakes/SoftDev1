"""Dessa Shapiro"""
import sudoku

def test_move_function():
    #Setup
    N = 4  
    puzzle = sudoku.make_puzzle(N)
    #invoke
    result = sudoku.move(puzzle, 0, 0, 2)
    moved_square = sudoku.get_square(puzzle, 0, 0)
    #analyze
    assert result is True
    assert moved_square['value'] == 2
    assert 2 in moved_square['row_set']
    assert 2 in moved_square['col_set']
    assert 2 in moved_square['reg_set']



