#   https://leetcode.com/problems/minimum-window-substring/?envType=daily-question&envId=2024-02-12

class Solution:
    #   TODO: could be more efficient
    def chars_are_in(self, sub:str, t:str):
        for c in t:
            if c not in sub:
                return False
        return True
    
    def minWindow(self, s: str, t: str) -> str:
        right = 0
        left = 0
        m = len(s)
        n = len(t)
        if n > m:
            return ""
        
        subs_that_contain = []
        
        #   while both pointers and in side the main string
        #   TODO: check about the validity of while right > left and terminate when left passes right
        while right < m and left < m:
            #   move right till we get everything inside
            while not self.chars_are_in(t=t, sub= s[left:right]):
                # if right >= m:
                #     break
                right += 1
            
            #   move left while we still contain everything to shorten
            while self.chars_are_in(t=t, sub= s[left:right]):
                subs_that_contain.append(s[left:right])
                # if left >= m:
                #     break
                left += 1
                
        
        #   if the initial conditions where never meet
        if not subs_that_contain:
            return ""
        
        return min(subs_that_contain, key=len)
    
if __name__ == "__main__":
    sol = Solution()
    s = "a"
    t = "a"
    print(sol.minWindow(s=s, t=t))