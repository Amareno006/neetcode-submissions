class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap: 
            self.timeMap[key].append((timestamp, value))
        else:
            self.timeMap[key] = [(timestamp, value)]

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap: 
            return ""
        else: 
            vals = self.timeMap[key]
        l = 0 

        r = len(vals) - 1
        while r >= l: 
            mid = (r + l) // 2

            if vals[mid][0] > timestamp: 
                r = mid - 1
            elif vals[mid][0] < timestamp: 
                l = mid + 1
            else: 
                return vals[mid][1]
        if r == -1: 
            return ""
        return vals[r][1]
