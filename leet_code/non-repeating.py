class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashtable = {}
        for char in s:
            if char in hashtable:
                hashtable[char] += 1
            else:
                hashtable[char] = 1

        for i, char in enumerate(s):
            if hashtable[char] == 1:
                return i

        return -1

if __name__ == '__main__':
     solution = Solution()
     assert solution.firstUniqChar("leetcode") == 0
     assert solution.firstUniqChar("loveleetcode") == 2
