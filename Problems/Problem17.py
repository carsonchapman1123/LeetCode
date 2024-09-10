from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        dic = {'2': ["a", "b", "c"],
               '3': ["d", "e", "f"],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        returnList = [""]
        for i in range(len(digits)):
            tempList = []
            currentNum = digits[i]
            currentLetters = dic[currentNum]
            for s in returnList:
                for letter in currentLetters:
                    tempList.append(s + letter)
            returnList = tempList
        return returnList

phone_number = "325"
print(Solution().letterCombinations(phone_number))
