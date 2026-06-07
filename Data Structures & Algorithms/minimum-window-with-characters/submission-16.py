class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s): 
            return ""

        min_value = len(s)
        res = ""
        window_t = {}

        window_s = {}
        for x in t:
            window_t[x] = 1 + window_t.get(x, 0)
     
        
        need = len(window_t)

        have = 0

        l = 0 

        for r in range(len(s)): 
            if s[r] in t:
                window_s[s[r]] = 1 + window_s.get(s[r], 0)
                if window_s[s[r]] == window_t[s[r]]:
                    have += 1


            while have == need: 
                if r - l + 1 <= min_value:
                    min_value = r - l + 1
                    res = s[l:r+1]
                if s[l] in window_t: 
                    window_s[s[l]] -= 1
                    if window_s[s[l]] < window_t[s[l]]:
                        have -=1

                l += 1
        return res

            
        