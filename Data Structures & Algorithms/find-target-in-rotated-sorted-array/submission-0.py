class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while r >= l: 
            mid = (l + r) // 2

            if nums[mid] == target: 
                return mid

            if target > nums[mid]: 
                if nums[r] < nums[mid]:
                    l = mid + 1
                elif nums[r] >= target: 
                    l = mid + 1
                else: 
                    r = mid - 1
            if target < nums[mid]: 
                if nums[r] > nums[mid]: 
                    r = mid - 1
                elif nums[r] >= target: 
                    l = mid + 1
                else: 
                    r = mid - 1


            


        return -1