class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}

        for index, num in enumerate(nums): 
            if num in my_dict:
                print(my_dict)
                return True

            my_dict[num] = index


        print(my_dict)
        return False

        