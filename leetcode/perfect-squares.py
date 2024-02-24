class Solution:
    def numSquares(self, n: int) -> int:
        #   start with 0
        queue = [(0, 0)]
        while queue:
            el = queue.pop(0)
            num = el[0]
            #   since max n is 10^4, expand potential children
            for i in range(1,100):
                res = num + i ** 2
                #   fast return found
                if res == n:
                    return el[1] + 1
                if res < n:
                    queue.append([res, el[1] + 1])
                if res > n:
                    break
                
if __name__ == "__main__":
    s = Solution()
    n = 7168
    print(s.numSquares(n))