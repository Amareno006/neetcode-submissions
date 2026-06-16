class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []



        for i, h in enumerate(heights):
            ind = i
            while stack and h < stack[-1][0]:
                res = max(res, stack[-1][0] * (i - stack[-1][1]))
                ind = stack[-1][1]
                stack.pop()
            stack.append((h, ind))
        for h, i in stack:
            res = max(res, h * (len(heights) - i))
        return res
            
