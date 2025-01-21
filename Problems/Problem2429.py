class Solution:
    def to_bin(self, n: int):
        return str(bin(n))[2:]

    def num_set_bits(self, n: int):
        return self.to_bin(n).count("1")

    def minimizeXor(self, num1: int, num2: int) -> int:
        num2_set_bits = self.num_set_bits(num2)
        num1_bin = list(self.to_bin(num1))
        num1_bin = ["0"] * (len(self.to_bin(num2)) - len(num1_bin)) + num1_bin
        num1_set_bits = self.num_set_bits(num1)
        i = len(num1_bin) - 1
        while num1_set_bits != num2_set_bits:
            if num1_set_bits < num2_set_bits and num1_bin[i] == "0":
                num1_bin[i] = "1"
                num1_set_bits += 1
            elif num2_set_bits < num1_set_bits and num1_bin[i] == "1":
                num1_bin[i] = "0"
                num1_set_bits -= 1
            i -= 1
        num1_bin = "".join(num1_bin)
        num1_bin = int(num1_bin, 2)
        return num1_bin

print(Solution().minimizeXor(25, 72))
