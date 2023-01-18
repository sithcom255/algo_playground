class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass

    def longest_palindrome_rec(self, s: str, l, r, offset) ->:
        if l - offset < 0 or r + offset >= len(s):
            return None


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome("bb"))
