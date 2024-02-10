class Solution:
    def is_polindrom(self, s: str) -> True:
        end = len(s) - 1
        if end == 0:
            return True
        
        i = 0
        while i < (len(s) / 2):
            if s[0 + i] != s[end - i]:
                return False
            i += 1
        return True
    
    def get_substrings(self, s:str) -> list:
        substrings = []
        #   getting all substrings
        for i in range(1, len(s) + 1):
                for j in range(len(s) - i + 1):
                    sub = s[j: j+i]
                    # print(f"i:{i}, j:{j} -> {sub}")
                    substrings.append(sub)
        
        return substrings

    def countSubstrings(self, s: str) -> int:
        # get all the sub strings
        subs = self.get_substrings(s)
        count = 0
        for sub in subs:
            if self.is_polindrom(sub):
                count += 1

        return count