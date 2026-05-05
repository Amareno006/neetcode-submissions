class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        valid_row = { i: {} for i in range(9)}
        valid_column = {i: {} for i in range(9)}
        valid_box = {(i, j): {} for i in range(3) for j in range(3)}
        for index, row in enumerate(board):
            for column, char in enumerate(row):
                box = (index // 3, column // 3)
                if char in valid_row[index] or char in valid_column[column] or char in valid_box[box]:
                    print(valid_row)
                    print(valid_column)

                    return False
                if char != ".":
                    valid_row[index][char] = 1
                    valid_column[column][char] = 1
                    valid_box[box][char] = 1
            

        
        print(valid_row)
        print(valid_column)
        return True