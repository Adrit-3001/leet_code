class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        starting = 0

        for i in range(len(nums)):
            if nums[i]:
                if starting != 0:
                    if i - starting - k < 0:    
                        return False
                    else:
                        starting = i + 1
                else:
                    starting = i + 1
        return True

