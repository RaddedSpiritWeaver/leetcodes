class Solution:
    def countSubstrings(self, s: str) -> int:
        # get all the sub strings
        sub_strings = []
        for l in range(len(s)):
            pass
        
def is_polindrom(s: str) -> True:
    end = len(s) - 1
    if end == 0:
        return True
    
    i = 0
    while i < (len(s) / 2):
        if s[0 + i] != s[end - i]:
            return False
        i += 1
    return True
        
if __name__ == "__main__":
    s = "aabcad"
    substrings = []
    #   getting all substrings
    for i in range(1, len(s) + 1):
            for j in range(len(s) - i + 1):
                sub = s[j: j+i]
                print(f"i:{i}, j:{j} -> {sub}")
                substrings.append(sub)
    print("----------------------------")        
    for ss in substrings:
        if is_polindrom(ss):
            print(ss)
