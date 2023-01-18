# User function Template for python3

class Solution:

    def __init__(self):
        self.memo = {}

    # Function to find length of longest increasing subsequence.
    def longestSubsequence(self, a, n):
        return self.rec(a, n - 1, 1000000000000)

    def rec(self, a, n, previous) -> int:



        return self.memo[n]

if __name__ == '__main__':
         # 1  2   2  3
    l = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5,
         13, 3, 11, 7, 15]
    print(Solution().longestSubsequence(l, len(l)))

