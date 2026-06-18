class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 0

        l = 1
        r = max(piles)

        while r >= l:
            currentHours = 0

            mid = (l + r) // 2
            for p in piles: 
                currentHours += math.ceil(p / mid)
            
            if currentHours <= h: 
                r = mid - 1
                res = mid
            elif currentHours > h: 
                l = mid + 1


        return res