from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        m, n = len(matrix[0]), len(matrix)
        l, r = 0, m * n - 1
        while l < r:
            k = self.get_half(l, r)
            mid_num = self.get_member_from_k(matrix, k, m)
            if mid_num > target:
                l, r = l, k
            elif mid_num == target:
                return True
            elif mid_num < target:
                l, r = k + 1, r

        if l == r:
            return self.get_member_from_k(matrix, l, m) == target

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
    print(Solution().searchMatrix([[1]], 1))
    print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
    print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60))
    print(Solution().searchMatrix([[1], [10], [23]], 10))
    print(Solution().searchMatrix([[1], [10], [23]], 10))
    print(Solution().searchMatrix([[1, 4], [2, 5]], 2))
