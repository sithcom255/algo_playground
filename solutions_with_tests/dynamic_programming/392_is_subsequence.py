class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = t_index = 0
        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1
        return s_index == len(s)



if __name__ == '__main__':
    solution = Solution()
    assert solution.isSubsequence("abc", "ahbgdc")
    assert not solution.isSubsequence("axc", "ahbgdc")
    assert not solution.isSubsequence("asdfasf", "a")
