from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[str]:
        listLength = len(words)
        if listLength == 0:
            return []
        wordLength = len(words[0])
        indices = []
        unusedWords = list(words)
        for i in range(0, len(s) - wordLength * listLength + 1):
            currSubstr = s[i:i + wordLength]
            if currSubstr in words:
                unusedWords.remove(currSubstr)
                for j in range(listLength - 1):
                    currSubstr = s[i + (j + 1) * wordLength:i + (j + 2) * wordLength]
                    if currSubstr in unusedWords:
                        unusedWords.remove(currSubstr)
                    else:
                        break
                if unusedWords == []:
                    indices.append(i)
                unusedWords = list(words)
        return indices


s = "barfoothefoobarman"
words = ["foo", "bar"]

print(Solution().findSubstring(s, words))
