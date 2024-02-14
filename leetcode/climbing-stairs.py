class Solution:
    cases = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n in self.cases:
            return self.cases[n]

        cursor = 3
        while cursor <= n:
            res = self.cases[cursor - 1] + self.cases[cursor - 2]
            self.cases[cursor] = res
            cursor += 1

        return self.cases[n]
    
class Solution2:
    def climb(self, n:int):
        if n == 1 or n == 2:
            return n
        return self.climb(n - 1) + self.climb(n - 2)
    
    def climbStairs(self, n: int) -> int:
        return self.climb(n)
    
if __name__ == "__main__":
    s = Solution2()
    r = s.climbStairs(44)
    print(r)