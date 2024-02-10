


class Solution:
    def countSubstrings(self, s: str) -> int:
        # get all the sub strings
        sub_strings = []
        for l in range(len(s)):
            pass
        
        
if __name__ == "__main__":
    s = "aabcad"
    #   getting all substrings
    for i in range(1, len(s) + 1):
            for j in range(len(s) - i + 1):
                print(f"i:{i}, j:{j} -> {s[j: j+i]}")
