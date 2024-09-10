class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        stack = []
        stackLength = 0
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
                stackLength += 1
            elif c in [")", "]", "}"]:
                if stackLength > 0 and stack[stackLength - 1] == closeToOpen[c]:
                    stack.pop(stackLength - 1)
                    stackLength -= 1
                else:
                    return False
        return stack == []

print(Solution().isValid("()[]"))
