class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        if len(s) == 0:
            return len(p) == 0
        if p == ".*":
            return True

        accepted = self.get_next(p, i)
        i += 1
        nxt = self.get_next(p, i)
        i += 1

        s_i = 0
        override = False
        while s_i < len(s):
            if accepted is None:
                return False
            ok, skip = self.consumable(s[s_i], accepted, nxt)
            if ok:
                if skip == 0:
                    override = self.get_next(p, i) is None
                s_i += 1
            if not ok and skip == 0:
                return False
            if skip == 1:
                accepted = nxt
                nxt = self.get_next(p, i)
                i += 1
            if skip == 2:
                accepted = self.get_next(p, i)
                i += 1
                nxt = self.get_next(p, i)
                i += 1
        print(i, len(p))
        return accepted is None or override

    def get_next(self, p, i):
        i += 1
        if i <= len(p):
            return p[i - 1]
        return None

    def consumable(self, s, accepted, next):
        print("in",s, accepted, next)
        if (s == accepted or accepted == ".") and next != "*":
            print("skipped 1")
            return True, 1
        if (s == accepted or accepted == ".") and next == "*":
            print("skipped 0")
            return True, 0
        if next == "*":
            print("skipped 2")
            return False, 2
        return False, 0

    #         edge case with 2 *

    # podivat se na character patternu
    # jestli je to pismenko, tak checknu a posunu se dal
    # jestli je to * tak se to muze opakovat predchozi pismeno
    # pokud je funkci repeating tak checkuju vuci valua, ale neberu hodnotu, kdyz je to false tak se posunu do dalsiho cyklu a nastavim repeating na false
    # pokud chybi misto v patternu tak je konec.
    # bude tam problem s tim ze .* muze matchnout hodne veci, takze tam budou nejake, ale nevypada to.


if __name__ == '__main__':
    assert not Solution().isMatch("", "a")
    assert Solution().isMatch("a", "a")
    assert Solution().isMatch("a", ".")
    assert Solution().isMatch("b", ".*")
    assert Solution().isMatch("bbbbb", ".*")
    assert Solution().isMatch("bb", "b*")
    assert Solution().isMatch("bbc", "a*b*c")
    assert Solution().isMatch("mississippi", "mis*is*ip*.")
    assert not Solution().isMatch("ab", ".*c")


