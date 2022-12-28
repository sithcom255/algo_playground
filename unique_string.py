class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = [None] * 256
        longest = [0,0]
        start = 0
        last = 0
        for i, elem in enumerate(s):
            if arr[ord(elem)] is None:
                arr[ord(elem)] = i
                last = i
                if longest[1] - longest[0] < last - start:
                    longest = [start, last]
            else:
                start = arr[ord(elem)] + 1
                arr[ord(elem)] = i
        print(longest)
        return s[longest[0]: longest[1] + 1]


def getnumber(character):
    return ord(character)

if __name__ == '__main__':
    obj = Solution()
    obj.lengthOfLongestSubstring("abcabcbb")