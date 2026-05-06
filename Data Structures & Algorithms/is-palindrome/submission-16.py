class Solution:
    def isPalindrome(self, s: str) -> bool:
        palind = ""
        s = s.lower()
        for n in s: 
            if n.isalnum():
                palind += n



        return palind == palind[::-1]
        