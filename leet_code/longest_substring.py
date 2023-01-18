class Solution:
    def longestSubstring(self, s: str, k: int):

        return self.longestSubstring_rec(s, k)

    def longestSubstring_rec(self, s: str, k: int):
        print("string", s)
        number_f = {}
        for char in s:
            if char in number_f:
                number_f[char] += 1
            else:
                number_f[char] = 1

        allowed_chars = {}
        for char in number_f:
            if number_f[char] >= k:
                allowed_chars[char] = 1

        max_lenght = 0
        current = 0
        for i, char in enumerate(s):
            if char not in allowed_chars:
                max_lenght = max(self.longestSubstring_rec(s[i - current:i], k), max_lenght)
                current = 0
            else:
                current += 1
        print("current", current)
        if current == len(s) and current >= k:
            max_lenght = len(s)
        elif current >= k:
            max_lenght = max(self.longestSubstring_rec(s[len(s) - current:len(s)], k), max_lenght)

        result = max_lenght
        return result


if __name__ == '__main__':
    solution = Solution()
    assert 3 == solution.longestSubstring("aaababcdbs", 3)
    assert 5 == solution.longestSubstring("ababbc", 2)
    assert 0 == solution.longestSubstring("ababacb", 3)
    assert 0 == solution.longestSubstring("aabcabb", 3)
    assert 3 == solution.longestSubstring("aacabbb", 3)
    assert 21 == solution.longestSubstring("zzzzzzzzzzaaaaaaaaabbbbbbbbhbhbhbhbhbhbhicbcbcibcbccccccccccbbbbbbbbaaaaaaaaafffaahhhhhiaahiiiiiiiiifeeeeeeeeee", 10)

