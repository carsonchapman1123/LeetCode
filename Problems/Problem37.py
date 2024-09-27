from typing import List

# Unsolved

class Solution:
    def get_box_number(self, row: int, column: int) -> int:
        """
        Returns the box number for a given tile at a given
        row and column. Box numbers begin at 0 for the top left tile
        and increase by one from left to right and top to bottom
        until bottom right box number 8 like so:

        0 1 2
        3 4 5
        6 7 8
        """
        return column // 3 + 3 * (row // 3)

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Add completed tiles to sets representing rows, columns,
        # and boxes.
        # Replace placeholders with lists from 1-9 representing
        # possible values that could be in that tile.
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == ".":
                    board[row][column] = set([str(x + 1) for x in range(9)])
                else:
                    rows[row].add(board[row][column])
                    cols[column].add(board[row][column])
                    box_number = self.get_box_number(row, column)
                    boxes[box_number].add(board[row][column])
        
        # Scan through board and eliminate incorrect answers
        # until correct ones are found.
        solved = False
        while not solved:
            set_seen = False
            for row in range(len(board)):
                for column in range(len(board[0])):
                    if isinstance(board[row][column], set):
                        set_seen = True
                        for n in board[row][column].copy():
                            if n in rows[row] or n in cols[column] or n in boxes[self.get_box_number(row, column)]:
                                board[row][column].remove(n)
                                if len(board[row][column]) == 1:
                                    print(rows[row])
                                    print(cols[column])
                                    print(boxes[self.get_box_number(row, column)])
                                    rows[row].add(n)
                                    cols[column].add(n)
                                    boxes[self.get_box_number(row, column)].add(n)
                                    board[row][column] = list(board[row][column])[0]
                                    print(board[row][column], "printed at", row, column)
                                    break
            #print(board)
            if not set_seen:
                solved = True
        print(board)


board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

s = Solution()
s.solveSudoku(board)
