class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        valid_row = { i: {} for i in range(9)}
        valid_column = {i: {} for i in range(9)}
        valid_box = {(i, j): {} for i in range(3) for j in range(3)}
        for index, row in enumerate(board):
            box_row = index // 3
            for column, char in enumerate(row):
                box = (box_row, column // 3)
                if char in valid_row[index] or char in valid_column[column] or char in valid_box[box]:
                    return False
                if char != ".":
                    valid_row[index][char] = 1
                    valid_column[column][char] = 1
                    valid_box[box][char] = 1

        return True