class Solution:
    def minimumLength(self, s: str) -> int:
        begin, end = 0, len(s) - 1
        
        while begin < end and s[begin] == s[end]:
            segment_char = s[begin]
            begin += 1
            end -= 1
            #   try to move begin
            while begin <= end and segment_char == s[begin]:
                begin += 1
            #   try to move end
            while begin <= end and segment_char == s[end]:
                end -= 1

        return end - begin + 1
    
if __name__ == "__main__":
    sol = Solution()
    s = "abbbbbbbbbbbbbbbbbbba"
    # s = 'aabccabba'
    # s = 'bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb'
    print(sol.minimumLength(s))