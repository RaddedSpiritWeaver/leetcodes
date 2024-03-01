from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            #   push value and index at the same time
            if not stack:
                stack.append((temperatures[i], i))
            else:
                #   when pushing to the stack, pop smaller values
                poped = []
                while stack[-1][0] < temperatures[i]:
                    poped.append(stack.pop())
                    if not stack: break
                #   for those poped values, process their result dif  
                for _ , j in poped:
                    res[j] = i - j
                stack.append((temperatures[i], i))
        return res
        
        
if __name__ == "__main__":
    sol = Solution()
    temperatures = [30,40,50,60]
    print(sol.dailyTemperatures(temperatures=temperatures))