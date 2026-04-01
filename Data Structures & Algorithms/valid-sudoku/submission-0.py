class Solution:
    def isValidLine(self, board, line):
        readset = set()
        for num in board[line]:
            if (num <="9" and num >="1"):
                if num in readset:
                    return False
                else:
                    readset.add(num)
        return True
    def isValidColumn(self, board, line):
        readset = set()
        for i in range(9):
            num = board[i][line]
            if (num <="9" and num >="1"):
                    if num in readset:
                        return False
                    else:
                        readset.add(num)
        return True

    def isValidBox (self, board, start_x_index, start_y_index):
        readset = set()
        for i in range(start_x_index,start_x_index+3 ):
            for j in range(start_y_index, start_y_index+3):
                num = board[i][j]
                if (num <="9" and num >="1"):
                    if num in readset:
                        return False
                    else:
                        readset.add(num)
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isValid = True
        # row 
        for row in range(9):
            isValid *= self.isValidLine(board, row)
            isValid *= self.isValidColumn(board, row)
        # column

        # box
        for i in range(0,9,3):
            for j in range(0,9,3):
                isValid *= self.isValidBox(board, i, j)
        return (isValid == 1)