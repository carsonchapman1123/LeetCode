from enum import Enum, auto

class Solution:
    class Direction(Enum):
        UP = auto()
        DOWN = auto()

    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        rows = [""] * numRows
        curr_row = 0
        curr_dir = self.Direction.DOWN
        for c in s:
            rows[curr_row] += c
            if curr_row == numRows - 1:
                curr_dir = self.Direction.UP
            elif curr_row == 0:
                curr_dir = self.Direction.DOWN
            if curr_dir == self.Direction.DOWN:
                curr_row += 1
            else:
                curr_row -= 1
        return "".join(rows)

print(Solution().convert("PAYPALISHIRING", 3))
