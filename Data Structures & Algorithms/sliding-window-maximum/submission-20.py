class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        window = list()
        res = []
        if k == 1: 
            return nums
        for r in range(len(nums)):
            if r - l + 1 > k: 
                window.pop(0)
                l += 1

            window.append(nums[r])

            if len(window) == k:
                res.append(max(window))     
        return res       
