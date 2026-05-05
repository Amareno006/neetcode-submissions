class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0
        nums.sort()

        consec_len = {}
        x = 1
        consec_len[x] = 1
        y = nums[0]
        for n in nums[1:]: 
            if n == y + 1:
                x+=1
                consec_len[x] = 1
            elif n != y: 
                x = 1
            y = n
        return max(consec_len)

        