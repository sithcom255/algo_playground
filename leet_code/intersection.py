class Solution:
    def intersect(self, nums1, nums2):
        counter1 = {}
        for number in nums1:
            if number in counter1:
                counter1[number] += 1
            else:
                counter1[number] = 1
        counter2 = {}
        for number in nums2:
            if number in counter2:
                counter2[number] += 1
            else:
                counter2[number] = 1
        smaller = counter1
        bigger = counter2
        if len(counter1) > len(counter2):
            smaller = counter2
            bigger = counter1
        result = []
        for num in smaller:
            if num in bigger:
                num_occurent = min(smaller[num], bigger[num])
                for x in range(num_occurent):
                    result.append(num)
        return result


if __name__ == '__main__':
    solution = Solution()
    assert [2, 2] == solution.intersect([1,2,2,1], [2,2])