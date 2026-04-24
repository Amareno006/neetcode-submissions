class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        target_dict = {}
        for index, value in enumerate(nums): 
            target_dict[target - value] = index
            if value in target_dict:
                x = nums.index(value)
                y = target_dict.get(value)
                print(target_dict)
                print(index)

        z = [min(x, y), max(x, y)]
        return  z