#   https://leetcode.com/problems/minimum-window-substring/?envType=daily-question&envId=2024-02-12

import copy
from collections import Counter

class Solution:
    def chars_are_in(self, s:Counter, t:Counter) -> bool:
        res = t - s
        #   cause 0 means all of t is in s and we want it to be true
        return not res
        
    
    def minWindow(self, s: str, t: str) -> str:
        right = 0
        left = 0
        m = len(s)
        n = len(t)
        s_counter = Counter("")
        t_counter = Counter(t)
        if n > m:
            return ""
        
        #   technically i could stop whenever i couldn't move the right or left pointers any more, and that would be the actual solution
        #   instead of returning the min
        subs_that_contain = []
        
        #   while both pointers and in side the main string
        #   TODO: check about the validity of while right > left and terminate when left passes right
        while right < m and left < m:
            #   move right till we get everything inside
            while (not self.chars_are_in(t=t_counter, s = s_counter)) and right < m:
                s_counter[s[right]] = s_counter[s[right]] + 1
                right += 1
            
            #   move left while we still contain everything to shorten
            while self.chars_are_in(t=t_counter, s = s_counter) and left < m:
                s_counter[s[left]] = s_counter[s[left]] - 1
                subs_that_contain.append(s[left:right])
                left += 1
                
        
        #   if the initial conditions where never meet
        if not subs_that_contain:
            return ""
        
        return min(subs_that_contain, key=len)
    
if __name__ == "__main__":
    sol = Solution()
    s = "aa"
    t = "aa"
    print(sol.minWindow(s=s, t=t))