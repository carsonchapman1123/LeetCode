class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return_str = "1"
        for i in range(1,n):
            num_to_count = {}
            keys = []
            for c in return_str:
                if c in keys:
                    num_to_count[c] += 1
                else:
                    keys.append(c)
                    num_to_count[c] = 1
            print num_to_count
            return_str = ""
            print keys
            for key in keys:
                return_str += str(num_to_count[key])
                return_str += key
        return return_str


print Solution().countAndSay(5)