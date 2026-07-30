class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i, (x, y) in enumerate(points): 
            euclid = (x**2) + (y**2)
            distances.append((euclid, i))

        
        heapq.heapify(distances)

        result = []
        for z in range(k): 
            val, res = heapq.heappop(distances)
            result.append(points[res])




        return result