import random


class Solution:
    def kthSmallest(self, arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        return self.kthSmallest2(arr, l, r, k - 1)

    def quicksort(self, arr, l, r):
        if l >= r:
            return
        rand = random.randint(l, r)
        arr[rand], arr[r] = arr[r], arr[rand]

        smaller = l


    def kthSmallest2(self, arr, l, r, k):
        if l >= r:
            return arr[k]
        rand = random.randint(l, r)
        arr[rand], arr[r] = arr[r], arr[rand]
        print(arr)

        smaller_equal = l
        for i in range(l, r + 1):
            print(arr[i], arr[r])
            if arr[i] <= arr[r]:
                arr[smaller_equal], arr[i] = arr[i], arr[smaller_equal]
                smaller_equal += 1

        # print(arr, arr[smaller_equal], arr[l: smaller_equal], smaller_equal)
        if smaller_equal > k:
            return self.kthSmallest2(arr, l, smaller_equal, k)
        elif smaller_equal == k:
            return arr[k]
        else:
            return self.kthSmallest2(arr, smaller_equal + 1, r, k)


if __name__ == '__main__':
    obj = Solution()
    print(obj.kthSmallest([7, 10, 4, 3, 20, 15], 0, 5, 3))
