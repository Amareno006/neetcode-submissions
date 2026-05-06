class Solution:
    def isPalindrome(self, s: str) -> bool:
        palind = ""
        for n in s: 
            if n.isalnum():
                palind += n.lower()
        for index, char in enumerate(palind):
            if char != palind[-1-index]:
                print(char, palind[-1 - index])
                print(palind)
                return False


        return True
        