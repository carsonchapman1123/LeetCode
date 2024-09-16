class Solution:
    def intToBin(self, n: int) -> str:
        return bin(n)[2:]

    def minBitFlips(self, start: int, goal: int) -> int:
        startBin = self.intToBin(start)
        startBinLen = len(startBin)
        goalBin = self.intToBin(goal)
        goalBinLen = len(goalBin)
        if startBinLen < goalBinLen:
            startBin = "0" * (goalBinLen - startBinLen) + startBin
        elif goalBinLen < startBinLen:
            goalBin = "0" * (startBinLen - goalBinLen) + goalBin
        diff = 0
        for i in range(max(startBinLen, goalBinLen)):
            if startBin[i] != goalBin[i]:
                diff += 1
        return diff
    
print(Solution().minBitFlips(10, 7))
