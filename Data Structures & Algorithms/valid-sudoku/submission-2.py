class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_store = defaultdict(set)
        col_store = defaultdict(set)
        box_store = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in row_store[row] or board[row][col] in col_store[col] or board[row][col] in box_store[(row // 3, col // 3)]:
                    return False
                row_store[row].add(board[row][col])
                col_store[col].add(board[row][col])
                box_store[((row // 3, col // 3))].add(board[row][col])
        return True


