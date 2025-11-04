from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        out = []
        for i in range (0, len(nums) - k + 1):
            subarr = nums[i:i+k]
            freq = {}
            add = 0
            for j in subarr:
                if j in freq:
                    freq[j] += 1
                else:
                    freq[j] = 1
            for m in range(0,x):
                if not freq: break
                max_key = max(freq, key=lambda k: (freq[k], k))
                add += max_key*freq[max_key]
                del freq[max_key]
            out.append(add)
        return out