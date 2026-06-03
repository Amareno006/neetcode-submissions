class Solution:
    def trap(self, height: List[int]) -> int:

        max_left = 0
        max_right = 0
        l = 0
        r = len(height) - 1
        count = 0
        while r > l: 
            max_left = max(max_left, height[l])
            max_right = max(max_right, height[r])
            if max_right > max_left:
                count += max_left - height[l]
                l += 1
            elif max_right <= max_left: 
                count += max_right - height[r]
                r-=1

        return count
