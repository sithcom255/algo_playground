class Solution:
    def __init__(self):
        self.steps = {1: 1, 2: 2}

    def climbStairs(self, n):
        if n in self.steps:
            return self.steps[n]
        if n - 2 not in self.steps and n > 2:
            self.climbStairs(n - 2)
        if n - 1 not in self.steps and n > 1:
            self.climbStairs(n - 1)

        result = self.steps[n - 1] + self.steps[n - 2]
        self.steps[n] = result
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(4))