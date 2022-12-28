class Solution:

    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        if N < M:
            return 0
        start, end = 0, 0
        for elem in A:
            if start < elem:
                start = elem
            end += elem
        result = 0
        while start <= end:
            print(start, end)
            mid = (start + end) // 2
            if is_valid(A, M, mid):
                result = mid
                end = mid - 1
            else:
                start = mid + 1
        return result


def is_valid(A, M, solution):
    students = 0
    total = 0
    for elem in A:
        if total + elem <= solution:
            total += elem
            continue
        students += 1
        total = elem
    print(students,)
    return students < M




#code here
if __name__ == '__main__':
    print(is_valid([15, 10, 19, 10, 5, 18, 7], 2, 30))
    # arr = [15, 17, 20]
    # N = 3
    # M = 2
    # obj = Solution()
    # print(obj.findPages(arr, N, M))
    # arr = [15, 10, 19, 10, 5, 18, 7]
    # print(obj.findPages(arr, 7, 5))

