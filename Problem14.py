class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        first = strs[0]
        returnStr = ""
        for i in range(len(first)):
            for j in range(1,len(strs)):
                if i == len(strs[j]) or strs[j][i] != first[i]:
                    return returnStr
            returnStr += first[i]
        return returnStr


test = ["aa", "a"]
print Solution().longestCommonPrefix(test)