from collections import defaultdict


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check if the column is valid
        # Check if the row is valid
        # Check if the 3x3 square is valid
        # There are 9 3x3 squares in 1 9x9 square
        # [[0,0],[0,1],[0,2]]
        # [[1,0],[1,1],[1,2]]
        # [[2,0],[2,1],[2,2]]
        row_map = defaultdict(set)  # Key is the row index
        col_map = defaultdict(set)  # Key is the column index
        square_map = defaultdict(set)  # Key is (row index / 3, col index / 3)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val.isnumeric():
                    if val in row_map[i] or val in col_map[j] or val in square_map[(i // 3, j // 3)]:
                        return False
                    row_map[i].add(val)
                    col_map[j].add(val)
                    square_map[(i // 3, j // 3)].add(val)

        return True
