class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            if num in my_dict: 
                my_dict[num] += 1
            else: 
                my_dict[num] = 1

        sorted_dict = sorted(my_dict, key = lambda k : my_dict[k], reverse="True")

        return sorted_dict[:k]
        
