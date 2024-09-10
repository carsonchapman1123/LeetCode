class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = 0
        for i in range(len(num1) - 1, -1, -1):
            this_line = 0
            for j in range(len(num2) - 1, -1, -1):
                this_line += int(num1[i]) * int(num2[j]) * 10**(len(num2) - 1 - j)
            this_line *= 10**(len(num1) - 1 - i)
            result += this_line
        return str(result)


print(Solution().multiply("100","100"))
