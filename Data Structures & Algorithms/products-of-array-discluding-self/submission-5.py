class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zeroes = 0
        cum_count = 1
        zero_spot = -1
        for index, num in enumerate(nums): 
            if num == 0: 
                num_zeroes += 1
                zero_spot = index
            else: 
                cum_count *= num

        if num_zeroes > 1:
            return [0] * len(nums)    
        list_returned = [0] * len(nums)
        if num_zeroes == 1: 
            list_returned[zero_spot] = cum_count
            return list_returned
        for index, num in enumerate(nums): 
            list_returned[index] = int(cum_count / num)
        return list_returned
        




        

