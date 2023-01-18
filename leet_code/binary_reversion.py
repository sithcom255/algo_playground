class Solution:
    def reverseBits(self, n: int):
        result = []
        for i in range(0, 32):
            if n % 2 == 1:
                result.append(1)
            else:
                result.append(0)
            n = n // 2
        x = 0
        print(result)
        for elem in result:
            x = (x << 1) + elem
        return x

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseBits(int("00000010100101000001111010011100", 2)))
