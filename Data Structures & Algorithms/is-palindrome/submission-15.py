class Solution:
    def isPalindrome(self, s: str) -> bool:
        palind = ""
        s = s.lower()
        for n in s: 
            if n.isalnum():
                palind += n
        for index, char in enumerate(palind):
            if char != palind[-1-index]:
                return False


        return True
        