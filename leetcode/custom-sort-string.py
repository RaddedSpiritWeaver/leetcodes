from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_counter = Counter(s)

        res = ""

        for char in order:
            if char in s:
                for _ in range(s_counter[char]):
                    res += char
                del s_counter[char]
        
        for k in s_counter:
            for _ in range(s_counter[k]):
                res += k
        
        return res
    
if __name__ == "__main__":
    sol = Solution()
    order = "cba"
    s = "abcd"
    print(sol.customSortString(order, s))