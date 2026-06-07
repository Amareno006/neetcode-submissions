class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        r, l = 0, 0
        max_count = 0
        char_seen = {}
        while r < len(s):
            char_seen[s[r]] = 1 +char_seen.get(s[r], 0)
            if (r-l+1) - max(char_seen.values()) > k:
                char_seen[s[l]] -= 1
                l += 1
            r += 1 
            max_count = max(max_count, r - l)

        return max_count

            