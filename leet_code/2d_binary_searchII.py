from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for cell in row:
                if cell == target:
                    return True

        return False

    def get_member(self, matrix, m, n):
        return matrix[n][m]

    def get_member_from_k(self, matrix, k, n):
        return matrix[(k // n)][(k % n)]

    def get_index(self, x, m, n):
        return n * m + x

    def get_half(self, l, r):
        return l + ((r - l) // 2)


if __name__ == '__main__':
    assert Solution().searchMatrix([[1]], 1)
    assert not Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
    assert Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60)
    print(Solution().searchMatrix([[1, 4], [2, 5]], 2))
