class Solution:
    def getSum(self, a: int, b: int) -> int:
        pass

    def get_binary(self, a: int):
        result = ''
        while a < 0:
            if a % 2 == 1:
                result = '1' + result
            else:
                result = '0' + result

if __name__ == '__main__':
    Solution().getSum(10,1)