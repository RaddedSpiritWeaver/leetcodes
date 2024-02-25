from typing import List
from collections import Counter
import math

#   answer is false if there are two numbers that are indivisible to each other, like 3 and 5, and have no
#   other common multiplicand

#   inspired by https://www.youtube.com/watch?v=0jNmHPfA_yE&t=466s
def primeFactors(n):
    res = set()
    while n % 2 == 0:
        res.add(2)
        n = n / 2
         
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0:
            res.add(i),
            n = n / i
             
    if n > 2:
        res.add(n)
    return res

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        c = Counter(nums)
        #   if there is a 1 in the list, then it always lands it its own group, so its false
        if c[1] > 0:
            #   unless the list is [1]
            if len(nums) == 1:
                return True
            return False
        if len(c) == 1:
            return True
        # #   to avoid duplicate numbers
        # nums = list(set(nums))
        #   initially everyone is in their own group
        group = [i for i in range(len(nums))]
        #   initially every root value is its self
        root_value = {i:nums[i] for i in range(len(nums))}

        def get_root(index):
            while group[index] != index:
                index = group[index]
            return index

        def join(i, j):
            #   get i parent root
            root_i = get_root(i)
            root_j = get_root(j)
            #   point root of j to i root
            group[root_j] = group[root_i]
            #   
            #   delete root j from the values
            

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if math.gcd(nums[i], nums[j]) > 1 and get_root(i) != get_root(j):
                    #   need to join their roots
                    join(i,j)
                    print((i,j))
                    
        #   if everything is in the same group then we return true
        roots = []
        for i in range(len(group)):
            roots.append(get_root(i))
            
        if len(Counter(roots)) == 1:
            return True

        return False
    
    #   we basically need one prime factor for each representative
    def b(self, nums: List[int]) -> bool:
        active_groups = set()
        for num in nums:
            #   try to see if it has a gcd greater than 1 with one of the groups
            marked = set()
            for g in active_groups:
                if math.gcd(g, num) > 1:
                    marked.add(g)
            if marked:
                #   if something was marked, then there should be a group merge
                active_groups = active_groups - marked
                primes = primeFactors(num)
                for x in marked:
                    primes = primes | primeFactors(x)
                add_me = 1
                for x in primes:
                    add_me *= x
                active_groups.add(int(add_me))
            else:
                active_groups.add(num)
        
        if len(active_groups) == 1:
            return True
        return False
        pass
        
        
        
if __name__ == "__main__":
    sol = Solution()
    # nums = [318,477,637,525,44,385,770,880,770,550,176,390,497,770,10,135,198,990,385,275,630,22,462,420,242,630,749,858,385,632,130,312,770,154,770,364,966,560,728,770,780,275,780,585,385,858,924,259,462,462,691,429,858,495,945,585,130,273,240,840,210,924,825,22,176,182,147,180,546,455,990,924,265,327,616,858,385,900,980,390,910,546,520,520,330,924,715,546,420,780,495,910,987,462,196,770,770,442,330,539,420,225,770,858,858,630,462,182,210,105,924,650,770,205,165,770,165,462,330,702,420,770,273,546,826,440,385,546,924,924,546,858,741,255,770,770,792,429,154,530,546,420,65,594,420,792,546,910,630,990,360,891,420,462,462,130,286,429,286,728,546,924,44,546,84,429,385,630,693,715,630,880,286,294,840,70,525,462,546,539,462,660,594,420,462,840,105,546,210,770,385,588,330,924,99,462,726,910,990,308,546,280,735,728,420,567,130,910,871,630,275,462,330,770,660,235,143,858,252,770,364,616,980,390,234,90,506,546,858,420,396,390,525,780,182,315,660,715,468,440,732,387,924,65,196,840,210,840,390,110,585,385,726,616,210,364,858,429,70,840,231,616,462,462,143,770,990,221,420,693,910,308,880,630,780,546,762,105,126,390,916,624,462,924,858,462,735,231,462,429,715,630,735,504,896,616,858,924,762,693,840,385,910,770,522,165,63,770,455,429,240,429,274,630,990,760,140,525,110,60,924,186,195,770,770,847,616,78,945,840,210,858,440,728,858,990,715,462,396,390,520,840,858,286,693,770,690,770,741,660,210,455,975,462,550,374,702,315,770,715,150,990,847,815,230,858,770,792,858,924,840,462,990,462,238,245,858,847,715,858,900,630,264,630,130,165,780,308,234,630,546,910,693,585,440,715,143,88,990,855,385,195,702,245,572,485,462,385,770,630,770,909,765,132,770,210,954,924,210,234,429,78,338,876,308,462,374,315,546,693,581,720,641,21,348,396,858,495,165,945,476,770,210,462,858,195,770,550,658,660,473,858,637,455,840,140,308,660,770,638,924,546,924,858,858,572,462,35,420,715,429,935,312,858,330,660,195,630,630,364,780,660,910,420,780,693,910,312,924,945,390,660,550,770]
    # nums = list(range(100_000))
    nums = [42,40,45,42,50,33,30,45,33,45,30,36,44,1,21,10,40,42,42]
    print(sol.b(nums))