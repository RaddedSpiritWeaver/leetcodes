from collections import Counter

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c = Counter(s)
        if c["1"] == 0:
            return ""
        res = ""
        for _ in range(c["1"] - 1):
            res += "1"
        for _ in range(c["0"]):
            res += "0"
        
        return res + ("1" if c["1"] != 0 else "")

if __name__ == "__main__":
    sol = Solution()
    s = "0001001"
    print(sol.maximumOddBinaryNumber(s))