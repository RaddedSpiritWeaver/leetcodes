from collections import Counter
from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        least_common = counter.most_common()[-1]
        key = least_common[0]
        val = least_common[1]
        while val <= k:
            k = k - val
            counter.pop(key)
            if(len(counter) == 0):
                break
            least_common = counter.most_common()[-1]
            key = least_common[0]
            val = least_common[1]

        return len(counter)


if __name__ == "__main__":
    s = Solution()
    arr = [5,5,4]
    k = 1
    print(s.findLeastNumOfUniqueInts(arr=arr, k=k))