from typing import List

"""
it is always optimal to use larger tokens to gain power and smaller tokens to get score
"""

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        #   first sort the tokens
        tokens.sort()
        
        #   make two pointers one for the smaller values, and one for the bigger values
        begin, end = 0, len(tokens) - 1
        max_score = score = 0
        
        #   we do a while until the pointers meet, or we run out of moves
        while begin <= end:
            if power >= tokens[begin]:
                power -= tokens[begin]
                begin += 1
                score += 1
                if score > max_score:
                    max_score = score
            elif score > 0:
                #   try to increase power
                power += tokens[end]
                end -= 1
                score -= 1
            else:
                # we dont have power to move begin or we dont have score to move end 
                break
        
        return max_score      
                
        
    
if __name__ == "__main__":
    sol = Solution()
    tokens = [100,200,300,400]
    power = 200
    print(sol.bagOfTokensScore(tokens, power))