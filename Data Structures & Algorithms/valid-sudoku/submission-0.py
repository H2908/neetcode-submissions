class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            for j in range(9):

                if board[i][j]=='.':
                    continue

                #row checking
                for col in range(j+1,9):
                    if board[i][j]==board[i][col]:
                        return False

                #column Checking
                for row in range(i+1,9):
                    if board[i][j]==board[row][j]:
                        return False

                # 3x3 Box Check
                startRow=(i//3)*3
                startCol=(j//3)*3

                for r in range(startRow, startRow + 3):
                    for c in range(startCol, startCol + 3):
                         # Skip the current cell
                        if r == i and c == j:
                            continue

                        if board[r][c] == board[i][j]:
                            return False

        return True

