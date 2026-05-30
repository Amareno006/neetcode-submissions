class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        height = 0
        maxHeight = []
        while r > l:
            height = (r - l) * min(heights[r], heights[l])
            maxHeight.append(height)
            if heights[r] > heights[l]:
                l += 1
            else: 
                r -= 1

        return max(maxHeight)      



