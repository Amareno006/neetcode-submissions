class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_seen = {}
        l, r = 0, 0
        max_len = 0
        while r < len(s): 
            if s[r] in char_seen:
                while s[r] in char_seen:
                    del char_seen[s[l]]
                    l += 1
            char_seen[s[r]] = r
            r += 1
            max_len = max(max_len, r-l)  
        return max_len