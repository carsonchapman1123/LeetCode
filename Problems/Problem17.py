class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        # dictionary of numbers to letters
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
                for l in currentLetters:
                    tempList.append(s + l)
            returnList = tempList
        return returnList

phone_number = "325"
print Solution().letterCombinations(phone_number)