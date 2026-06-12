class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = []

        index = []

        for i, r in enumerate(temperatures): 
            
            while stack and r > stack[-1]:
                result[index[-1]] = i - index[-1] 
                stack.pop()
                index.pop()
            stack.append(r)
            index.append(i)

        return result
