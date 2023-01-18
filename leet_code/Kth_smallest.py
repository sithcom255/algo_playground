from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rec = self.kth_smallest_rec(matrix, 0, len(matrix) - 1)

        return rec[k - 1]

    def kth_smallest_rec(self, matrix, l, r):
        print("hello", l, r)
        if r - l == 0:
            return matrix[r]
        if r < l:
            return []


        middle = (r - l) // 2
        l_arr = self.kth_smallest_rec(matrix, l, l + middle)
        r_arr = self.kth_smallest_rec(matrix, l + middle + 1, r)

        return self.merge(l_arr, r_arr)

    def merge(self, l_arr, r_arr):
        result = []

        while l_arr or r_arr:
            if l_arr:
                if r_arr:
                    if l_arr[0] <= r_arr[0]:
                        result.append(l_arr.pop(0))
                    else:
                        result.append(r_arr.pop(0))
                else:
                    result.append(l_arr.pop(0))
            elif r_arr:
                result.append(r_arr.pop(0))

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([3, 6, 7], [9, 10, 11]))
    print(solution.kthSmallest([[3, 6, 7], [1, 2, 4], [8, 9, 10]], 4))
    print(solution.kthSmallest(
        [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
        , 4))
