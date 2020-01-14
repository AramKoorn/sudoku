import numpy as np
from __future__ import division
import properties

np.zeros(shape=(9, 9))


class Sudoku:
    def __init__(self):
        pass

    @property
    def make_puzzle(self):
        s = ('8 64 3    5     7     2    '
            '32  8  5   8 5 4  1   7  93'
            '    4     9     4    6 72 8')
        grid = [x for x in s]
        puzzle = np.array(grid).reshape((9, 9))
        puzzle = np.where(puzzle == ' ', 0, puzzle).astype('int')
        return puzzle


    @property
    def make_grid_dict(self):
        grid = '''\
        AA AB AC BA BB BC CA CB CC
        AD AE AF BD BE BF CD CE CF
        AG AH AI BG BH BI CG CH CI
        DA DB DC EA EB EC FA FB FC
        DD DE DF ED EE EF FD FE FF
        DG DH DI EG EH EI FG FH FI
        GA GB GC HA HB HC IA IB IC
        GD GE GF HD HE HF ID IE IF
        GG GH GI HG HH HI IG IH II
        '''
        grid = grid.split()
        all_elements = [x for x in range(81)]
        dict_grid = dict(zip(all_elements, grid))
        return dict_grid


class Solver(Sudoku):
    def __init__(self):
        self.puzzle = self.make_puzzle
        pass


    def find_first_zero(self):
        field = self.make_puzzle
        field = field.flatten()

        for i, x in enumerate(field):
            if x == 0:
                return i


    def get_vertical(self, element):
        vertical_array = puzzle[:,1]


    def get_horizontal(self, self, element):
        return horizontal_array

    def get_block_array(self):
        pass






    def backtracking(self):
        element = self.find_first_zero()
        print(element)






