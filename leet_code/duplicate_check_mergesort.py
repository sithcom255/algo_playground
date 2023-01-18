class Solution:
    def containsDuplicate(self, nums):
        return mergesort(nums, 0, len(nums) - 1)

# 0 2 3 5
# 0 1, 2 2 , 3 4, 5 5,

def mergesort(nums, l_index, r_index):
    middle = (r_index - l_index) // 2
    if middle < 1:
        return nums
    middle += l_index
    l, r = nums[l_index: middle + 1], nums[middle + 1, r_index + 1]
    l, l_duplicate = mergesort(nums, l_index, middle)
    r, r_duplicate = mergesort(nums, middle + 1, r_index)
    if l_duplicate or r_duplicate:
        return [], True
    result = []
    while l or r:
        if l and r:
            if l[0] < r[0]:
                result.append(l[0])
                l.pop(0)
            elif l[0] == r[0]:


        elif l:

        elif r:


if __name__ == '__main__':
    solution = Solution()
    assert solution.containsDuplicate([1, 2, 3, 4, 5, 1])
