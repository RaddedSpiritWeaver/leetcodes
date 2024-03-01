from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            if not stack:
                stack.append((temperatures[i], i))
            else:
                while stack[-1][0] < temperatures[i]:
                    _ , j = stack.pop()
                    res[j] = i - j
                    if not stack: break
                stack.append((temperatures[i], i))
        return res
        
        
if __name__ == "__main__":
    sol = Solution()
    temperatures = [30,40,50,60]
    print(sol.dailyTemperatures(temperatures=temperatures))