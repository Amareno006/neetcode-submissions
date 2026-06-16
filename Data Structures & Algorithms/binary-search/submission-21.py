class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while  r >= l:
            index = (r + l) // 2
            if nums[index] > target:
                r  = index - 1
            elif nums[index] < target: 
                l = index + 1
            elif nums[index] == target: 
                return index


        return -1

