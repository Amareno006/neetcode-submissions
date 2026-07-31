class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        window = []
        freq = {}
        for x in tasks: 
            if x in freq: 
                freq[x] += 1
            else: 
                freq[x] = 1

        for z in freq.values(): 
            window.append(-z)


        cooldown = []

        heapq.heapify(window)

        res = 0
        while window: 
            cooldown = []

            for _ in range(n+1): 
                if not window and not cooldown: 
                    break

                if window:     
                    val = heapq.heappop(window) + 1
                    if val != 0: 
                        cooldown.append(val)
                res += 1
            for x in cooldown: 
                heapq.heappush(window, x)
            
        return res
