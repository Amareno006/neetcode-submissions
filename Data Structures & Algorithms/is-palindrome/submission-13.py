class Solution:
    def isPalindrome(self, s: str) -> bool:
        palind = ""
        for n in s: 
            if n.isalnum():
                palind += n.lower()
        for index, char in enumerate(palind):
            if char != palind[-1-index]:
                return False


        return True
        