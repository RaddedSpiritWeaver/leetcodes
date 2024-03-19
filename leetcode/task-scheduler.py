from typing import List
import heapq
from collections import Counter, defaultdict


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        queue = []
        for key, val in c.items():
            heapq.heappush(queue, (-1 * val, key))
        
        last_seen = defaultdict(lambda: -1)
        time = 0
        while queue:
            passed = []
            while queue:
                item = heapq.heappop(queue)
                priority, key = item[0], item[1]
                if last_seen[key] < 0 or (time - last_seen[key] - 1) >= n:
                    last_seen[key] = time
                    priority += 1
                    if priority != 0:
                        #   we are not done with this task
                        passed.append((priority, key))
                    break
                else:
                    passed.append(item)
            queue += passed
            heapq.heapify(queue)
            time += 1
        
        return time

    
if __name__ == "__main__":
    sol = Solution()
    tasks = ["A","A","A","B","B","B"]
    n = 3
    print(sol.leastInterval(tasks, n))