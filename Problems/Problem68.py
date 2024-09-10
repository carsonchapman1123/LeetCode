from typing import List

import math

class Solution:
    def helper(self, words: List[str], maxWidth: int, totalWidth: int) -> str:
        """
        Takes a list of words and returns them as a string of length
        maxWidth with spaces properly applied.
        """
        if len(words) == 1:
            return words[0] + " " * (maxWidth - totalWidth)
        result = ""
        numSpaces = max(len(words) - 1, 1)
        numSpaceChars = maxWidth - totalWidth
        for i in range(len(words)):
            numSpaces = 0 if (len(words) - 1 - i) == 0 else math.ceil(numSpaceChars / (len(words) - 1 - i))
            result += words[i]
            result += " " * numSpaces
            numSpaceChars -= numSpaces
        return result
    
    def final_line_helper(self, words: List[str], maxWidth):
        """
        Formats the final line.
        """
        final_line = " ".join(words)
        return final_line + " " * (maxWidth - len(final_line))

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        currentWords = []
        currentLength = 0
        for i in range(len(words)):
            if len(words[i]) + currentLength + len(currentWords) > maxWidth:
                result.append(self.helper(currentWords, maxWidth, currentLength))
                currentWords = [words[i]]
                currentLength = len(words[i])
            else:
                currentWords.append(words[i])
                currentLength += len(words[i])
        if len(currentWords) > 0:
            result.append(self.final_line_helper(currentWords, maxWidth))
        return result

print(Solution().fullJustify(["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"], 16))
