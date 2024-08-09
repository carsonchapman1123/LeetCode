from collections import deque

class Solution(object):
    # Returns the length of the longest substring with unique characters.
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = deque()
        length = len(s)
        longest = 0
        for i in range(length):
            if s[i] not in substr:
                substr.append(s[i])
            else:
                while substr[0] != s[i]:
                    substr.popleft()
                substr.popleft()
                substr.append(s[i])
            longest = max(longest, len(substr))
        return longest

print(Solution().lengthOfLongestSubstring("abcabcaa"))
