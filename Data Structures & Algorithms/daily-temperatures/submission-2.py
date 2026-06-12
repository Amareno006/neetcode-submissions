class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = []


        for i, r in enumerate(temperatures): 
            
            while stack and r > temperatures[stack[-1]]:
                index = stack.pop()

                result[index] = i - index

            stack.append(i)


        return result
