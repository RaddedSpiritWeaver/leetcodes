from collections import Counter

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c = Counter(s)
        ones = ["1" for _ in range(c["1"])]
        zeros = ["0" for _ in range(c["0"])]
        res = ones[:len(ones) - 1] + zeros + ones[len(ones) - 1:len(ones)]
        return "".join(res)

if __name__ == "__main__":
    sol = Solution()
    s = "0001001"
    print(sol.maximumOddBinaryNumber(s))