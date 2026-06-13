class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))                         
        times = [(target-p)/s for p, s in cars]
        print(times)
        fleet = 0
        state = 0
        for t in reversed(range(len(times))):
            if state < times[t]:
                fleet += 1
                state = times[t]

        return fleet