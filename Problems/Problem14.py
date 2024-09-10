from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ret
            ret += first[i]
        return ret

test = ["flow", "flight"]
print(Solution().longestCommonPrefix(test))
