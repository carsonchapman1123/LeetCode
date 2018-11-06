class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        height = len(matrix)
        result = []
        if height == 0:
            return result
        width = len(matrix[0])
        if height == 1:
            return matrix[0]
        if width == 1:
            for n in matrix:
                result.append(n[0])
            return result
        i = 0
        j = 0
        dir = 0
        while width > 0 and height > 0 and matrix[i][j] is not None:
            result.append(matrix[i][j])
            matrix[i][j] = None
            if dir == 0:
                j += 1
                if j == width - 1 or matrix[i][j+1] is None:
                    dir += 1
            elif dir == 1:
                i += 1
                if i == height - 1 or matrix[i+1][j] is None:
                    dir += 1
            elif dir == 2:
                j -= 1
                if j == 0 or matrix[i][j-1] is None:
                    dir += 1
            elif dir == 3:
                i -= 1
                if i == 0 or matrix[i-1][j] is None:
                    dir = 0
        return result


test = [[1,2,3],
        [8,9,4],
        [7,6,5]]

print Solution().spiralOrder(test)