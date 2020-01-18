__author__ = ' Aram'

import numpy as np
from itertools import compress
import math

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
        values = list(range(1, 10))

        pass


    def find_empty_cells(self):
        field = self.make_puzzle
        select = field.flatten() == 0
        index_list = list(compress(list(range(81)), select))

        return index_list


    def check_horizontal(self, element, puzzle):
        puzzle = puzzle.reshape((9, 9))
        index_row = math.floor(element/9)
        check_row = list(puzzle[index_row ,:])
        check_row = list(filter(lambda a: a != 0, check_row))

        if len(check_row) == len(set(check_row)):
            return True
        else:
            return False


    def check_vertical(self, element, puzzle):

        if element < 9:
            index_column = element
        else:
            index_column = element % 9

        check_vertical = list(puzzle[:, index_column])
        check_vertical = list(filter(lambda a: a != 0, check_vertical))

        if len(check_vertical) == len(set(check_vertical)):
            return True
        else:
            return False


    def check_block(self, element, puzzle):
        dict_grid = self.make_grid_dict
        first_letter = dict_grid[element].split()[0][0]
        dict_grid_rev = dict(zip(dict_grid.values(), dict_grid.keys()))
        k = [k for k in dict_grid_rev.keys() if k.startswith(first_letter)]
        check_block = list({key: dict_grid_rev[key] for key in k}.values())
        check_block = puzzle.flatten()[check_block]
        check_block = list(filter(lambda a: a != 0, check_block))

        if len(check_block) == len(set(check_block)):
            return True
        else:
            return False


    def validate(self, element, candidate_value, puzzle):
        tmp_puzzle = puzzle.flatten()
        np.put(tmp_puzzle, [element], [candidate_value])
        bool_hor = self.check_horizontal(element, puzzle)
        bool_vert = self.check_vertical(element, puzzle)
        bool_block = self.check_block(element, puzzle)

        if all([bool_hor, bool_vert, bool_block]):
            return True
        else:
            return False


    def back_tracking(self):


        dict_res = {}
        values = list(range(1, 10))
        candidates = self.find_empty_cells()
        element = 1
        candidate_value = 1
        bool_insert = self.validate(element, candidate_value, self.puzzle)


if __name__ == '__main__':
    Solver().back_tracking()