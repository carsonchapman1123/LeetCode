from typing import List

class Solution(object):
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = []
        if n == 0:
            return result
        if n == 1:
            return [[1]]
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(0)
            result.append(temp)
        current = 1
        row = 0
        col = 0
        dir = 0
        while current <= n * n:
            result[row][col] = current
            if dir == 0:
                col += 1
                if col == n - 1 or result[row][col + 1] != 0:
                    dir += 1
            elif dir == 1:
                row += 1
                if row == n - 1 or result[row + 1][col] != 0:
                    dir += 1
            elif dir == 2:
                col -= 1
                if col == 0 or result[row][col - 1] != 0:
                    dir += 1
            elif dir == 3:
                row -= 1
                if row == 0 or result[row - 1][col] != 0:
                    dir -= 3
            current += 1
        return result

print(Solution().generateMatrix(4))