class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []

        while nums: 
            x = nums.pop()

            heapq.heappush(res, x)
            

            if len(res) > k:
                heapq.heappop(res)
        return res[0]
