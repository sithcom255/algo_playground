class Solution:
    def missingNumber(self, nums):
        expected = ((len(nums) + 1) * (len(nums) ))// 2
        for i in nums:
            expected -= i
        return  expected

if __name__ == '__main__':
    solution = Solution()
    print(solution.missingNumber([i for i in range(0, 100)]))
