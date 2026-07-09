class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        res = 0

        seen = set()

        for n in nums: 
            if n in seen: 
                res = n
            seen.add(n)

        return res

        
        