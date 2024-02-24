from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1

        l = [(char, freq[char]) for char in freq.keys()]
        l.sort(key= lambda x: x[1], reverse = True)
        res = ""
        for char, count in l:
            for _ in range(count):
                res = res + char
        
        return res
    
if __name__ == "__main__":
    sol = Solution()
    s = "tree"
    print(sol.frequencySort(s))