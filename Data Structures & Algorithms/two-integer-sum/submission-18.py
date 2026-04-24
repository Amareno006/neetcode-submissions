class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        target_dict = {}
        for index, value in enumerate(nums): 

            if value in target_dict:
                x = index
                y = target_dict.get(value)
                print(target_dict)
                print(index)
                return [target_dict.get(value), index]
            target_dict[target - value] = index
