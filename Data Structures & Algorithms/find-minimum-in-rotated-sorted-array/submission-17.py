class Solution:
    def findMin(self, nums: List[int]) -> int:

        res = 0
        l = 0 
        r = len(nums) - 1

        while r > l:
            mid = (l + r) // 2
            if nums[mid] < nums[r] : 
                r = mid
            else:
                l = mid + 1
 
        return nums[l]

        