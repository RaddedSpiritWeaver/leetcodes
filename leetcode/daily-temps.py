from traitlets import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures) - 1):
            j = 1
            while temperatures[i] >= temperatures[i + j]:
                j += 1
                if i + j >= len(temperatures):
                    break
            else:
                res[i] = j
        return res
        
        
if __name__ == "__main__":
    sol = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    print(sol.dailyTemperatures(temperatures=temperatures))