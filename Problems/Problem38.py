class Solution:
    def countAndSay(self, n: int) -> int:
        return_str = "1"
        for i in range(1, n):
            num_to_count = {}
            keys = []
            for c in return_str:
                if c in keys:
                    num_to_count[c] += 1
                else:
                    keys.append(c)
                    num_to_count[c] = 1
            return_str = ""
            for key in keys:
                return_str += str(num_to_count[key])
                return_str += key
        return return_str


print(Solution().countAndSay(5))
