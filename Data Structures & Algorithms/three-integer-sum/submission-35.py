class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_list = []

        nums.sort()
        for i in range(0, len(nums) -2):
            r = len(nums) - 1
            l = i + 1

            while r > l: 
                if nums[r] + nums[l] + nums[i] > 0: 
                    r -= 1
                elif nums[r] + nums[l] + nums[i] < 0: 
                    l += 1
                else: 
                    if [nums[i], nums[l], nums[r]] not in num_list: 
                        num_list.append([nums[i], nums[l], nums[r]])
                    r -= 1

        return num_list 
        