class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        target_dict = {}
        for index, value in enumerate(nums): 

            if value in target_dict:
                return [target_dict[value], index]
            target_dict[target - value] = index