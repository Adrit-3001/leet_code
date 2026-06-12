class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = nums[0]
        n = len(nums)
        nums_c = nums
        k = 1

        for i in range(1, n):
            if seen != nums[i]:
                seen = nums[i]
                k += 1
                nums_c[k - 1] = seen
        nums = nums_c
        return k