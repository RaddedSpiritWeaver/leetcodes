from timeit import default_timer as timer

class Solution:
    def numSquares(self, n: int) -> int:
        #   start with 0
        queue = [(0, 0)]
        while queue:
            el = queue.pop(0)
            num = el[0]
            #   since max n is 10^4, expand potential children
            rng = list(range(1,101))
            rng = rng[::-1]
            for i in rng:
                res = num + i ** 2
                #   fast return found
                if res == n:
                    return el[1] + 1
                if res < n:
                    queue.append([res, el[1] + 1])
                if res > n:
                    continue
                
if __name__ == "__main__":
    start = timer()
    s = Solution()
    n = 7168
    print(s.numSquares(n))
    end = timer()
    print(start - end)