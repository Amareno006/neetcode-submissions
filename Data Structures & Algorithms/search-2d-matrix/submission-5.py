class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
                
        bottom = 0 
        top = len(matrix) - 1

        while top >= bottom: 
            middle = (top + bottom) // 2

            if matrix[middle][0] > target: 
                top = middle - 1
            elif matrix[middle][-1] < target: 
                bottom = middle + 1
            else: 
                break



        if bottom > top: 
            return False

        l, r = 0, len(matrix[0]) - 1

        row = (bottom + top) // 2


        while r >= l: 
            mid = (r + l) // 2

            if matrix[row][mid] < target: 
                l = mid + 1
            elif matrix[row][mid] > target: 
                r = mid - 1
            else: 
                return True

        return False

            