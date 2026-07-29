class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        inv_stones = [-z for z in stones]
        heapq.heapify(inv_stones)
        while inv_stones: 
            if len(inv_stones) == 1: 
                return -inv_stones[0]

            x = heapq.heappop(inv_stones)
            y = heapq.heappop(inv_stones)

            if x != y: 
                heapq.heappush(inv_stones,-(abs(x-y)))





        
        return 0