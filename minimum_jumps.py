class Solution:
    def minJumps(self, arr, n):
        if len(arr) == 0:
            return 0

        minimum_steps = 1
        current = 0
        steps = arr[0]

        for _ in range(len(arr)):

            if steps + current >= len(arr) - 1:
                return minimum_steps

            max_ = 0
            max_i = 0

            for i in range(steps):
                if (arr[current + i + 1] - steps + 1 + i) > max_:
                    max_ = arr[current + i + 1] - steps + 1 + i
                    max_i = current + i + 1

            current = max_i

            steps = arr[max_i]

            minimum_steps += 1
            if max_ == 0:
                return - 1


if __name__ == '__main__':
    obj = Solution()
    print(obj.minJumps(
        [85, 59, 94, 21, 33, 35, 67, 57, 44, 28, 69, 86, 37, 78, 54, 94, 14, 48, 25, 83, 18, 59, 33, 28, 99, 25, 81, 46,
         77, 51, 39, 62, 9, 32, 49, 43, 33, 15, 100, 77, 9, 68, 28, 47, 12, 82, 6, 26, 96, 98, 75, 13, 57, 7, 8, 55, 33,
         55, 0, 76, 5, 5, 3, 15, 3, 53, 58, 36, 34, 23, 79, 10, 57, 6, 23, 69, 54, 29, 61, 49, 27, 36, 63, 84, 9, 71, 4,
         8, 25, 71, 85, 97, 77, 88, 11, 46, 6, 35, 83, 7], 11))
