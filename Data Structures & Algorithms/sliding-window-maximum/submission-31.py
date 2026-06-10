class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        window = list()
        res = []

        for r in range(len(nums)):

            while window and nums[r] > nums[window[-1]]:
                window.pop()
            window.append(r)
            if window[0] < l: 
                window.pop(0)
            if r - l + 1 == k:
                res.append(nums[window[0]])
                l+= 1  
        return res        
