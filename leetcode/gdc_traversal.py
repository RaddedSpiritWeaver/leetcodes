from functools import cache
from typing import List
from collections import Counter, defaultdict
import math

#   answer is false if there are two numbers that are indivisible to each other, like 3 and 5, and have no
#   other common multiplicand

#   inspired by https://www.youtube.com/watch?v=0jNmHPfA_yE&t=466s
@cache
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
        c = Counter(nums)
        #  if there is a 1 in the list, then it always lands it its own group, so its false
        if c[1] > 0:
            #   unless the list is [1]
            if len(nums) == 1:
                return True
            return False
        
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
    
    def c(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        c = Counter(nums)
        
        #  if there is a 1 in the list, then it always lands it its own group, so its false
        if c[1] > 0:
            return False
        
        prime_factors = defaultdict(list)
        prime_to_node = defaultdict(list)
        
        for i in range(len(nums)):
            num = nums[i]
            res = set()
            while num % 2 == 0:
                res.add(2)
                num = num // 2
                
            for j in range(3,int(num ** 0.5)+1,2): 
                while num % j== 0:
                    res.add(j),
                    num = num // j
                    
            if num > 2:
                res.add(num)
            
            prime_factors[i] = list(res)
            for p in res:
                prime_to_node[p].append(i)
        
        #   now bfs to go through
        visited = set()
        traversable = set()
        if len(list(prime_to_node.keys())) == 0:
            return False
        first_prime = list(prime_to_node.keys())[0]
        queue = [first_prime]
        #   TODO: do it with bfs as well
        while queue:
            prime = queue.pop(0)
            #   add this prime to the visited set
            visited.add(prime)
            traversable = traversable | set(prime_to_node[prime])
            for node in prime_to_node[prime]:
                #   add the unvisited prime numbers for those nodes
                for pp in prime_factors[node]:
                    if pp not in visited and pp not in queue:
                        queue.append(pp)

        return len(traversable) == len(nums)
        
                    

    
# lcm_all = num
#                 for x in marked:
#                     lcm_all = math.lcm(lcm_all, x)
#                 active_groups.add(int(lcm_all))    
        
if __name__ == "__main__":
    sol = Solution()
    nums = [42,40,45,42,50,33,30,1,45,33,45,30,36,44,21,10,40,42,42]
    print(sol.c(nums))