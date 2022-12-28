class Solution:
    def __init__(self):
        self.board = []
        self.squares = []
        self.rows = []
        self.columns = []

    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.get_initial_squares(board)
        self.rows = []
        self.columns = []

        for i in range(len(board)):
            self.rows.append(set(str(i + 1) for i in range(9)))
            self.columns.append(set(str(i + 1) for i in range(9)))
        for i, y in enumerate(board):
            for j, x in enumerate(y):
                if x == ".":
                    continue
                else:
                    self.rows[i].remove(x)
                    self.columns[j].remove(x)

        self.backtracking_solution(0, 0)
        return self.board

    def backtracking_solution(self, x, y) -> bool:
        if self.board[y][x] != ".":
            if x + 1 < 9:
                return self.backtracking_solution(x + 1, y)
            elif y + 1 < 9:
                return self.backtracking_solution(0, y + 1)
            else:
                return True

        available = self.get_square(x, y).intersection(self.rows[y]).intersection(self.columns[x])

        if not available:
            return False

        if x == 8 and y == 8 and len(available) == 1:
            self.board[y][x] = list(available)[0]
            return True

        for possible in available:
            self.board[y][x] = possible
            self.get_square(x, y).remove(possible)
            self.rows[y].remove(possible)
            self.columns[x].remove(possible)
            res = None
            if x + 1 < 9:
                res = self.backtracking_solution(x + 1, y)
            else:
                res = self.backtracking_solution(0, y + 1)
            if not res:
                self.get_square(x, y).add(possible)
                self.rows[y].add(possible)
                self.columns[x].add(possible)
                continue
            return True
        self.board[y][x] = "."
        return False

    def get_square(self, x, y):
        return self.squares[(y // 3) * 3 + (x // 3)]

    def get_initial_squares(self, board):
        squares = []
        for i in range(9):
            squares.append(set(str(i + 1) for i in range(9)))
        self.squares = squares
        for y in range(len(board)):
            for x in range(len(board)):
                if board[y][x] != ".":
                    set_ = self.get_square(x, y)
                    set_.remove(board[y][x])


if __name__ == '__main__':
    obj = Solution()
    obj.solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                     [".", "9", "8", ".", ".", ".", ".", "6", "."],
                     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                     [".", "6", ".", ".", ".", ".", "2", "8", "."],
                     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                     [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
