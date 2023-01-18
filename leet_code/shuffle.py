from typing import List
from random import randint
class Solution:

    def __init__(self, nums: List[int]):
        self.reset_backup = nums.copy()
        self.nums = nums

    def reset(self) -> List[int]:
        self.nums = self.reset_backup.copy()
        return self.nums


    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            r = randint(i, len(self.nums))
            self.nums[i], self.nums[r] = self.nums[r], self.nums[i]
        return self.nums



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()