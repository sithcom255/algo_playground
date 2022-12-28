#User function Template for python3
class Solution:

    def maxSortedAdjacentDiff(self,arr, n):
        max = float('-inf')
        min = float('inf')
        for elem in arr:
            if elem > max:
                max = elem
            if elem < min:
                min = elem
        range_size = max - min
        size = range_size // (len(arr) + 1) + 1
        buckets = [None] * (len(arr) + 1)
        for i, elem in enumerate(arr):
            buckets[elem//size] = insert_to_bucket(buckets[elem//size], elem)
        print(size, buckets)
        last = 0
        tracing = False
        max_num = 0
        for i in range(len(buckets)):
            if buckets[i] is None:
                if tracing:
                    continue
                else:
                    last = buckets[i - 1][-1]
                    tracing = True
            elif tracing:
                max_ = buckets[i][0] - last
                if max_ > max_num:
                    max_num = max_
                tracing = False
        return max_num


def insert_to_bucket(arr, number):
    print(number, arr)
    if arr is None:
        return [number]
    elif len(arr) == 1:
        if arr[0] < number:
            arr.append(number)
        elif arr[0] > number:
            arr.insert(0, number)
    elif len(arr) == 2:
        if arr[0] > number:
            arr[0] = number
        elif arr[1] < number:
            arr[1] = number
    return arr


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxSortedAdjacentDiff([1, 2, 3, 4, 5], 5))
