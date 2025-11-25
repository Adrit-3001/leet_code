class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        num = 0
        if k % 2 == 0 or k % 5 == 0: return -1

        for i in range(k):
            num = (num*10 + 1) % k
            if num == 0: return i +% k == 0: return len(num)
            num += "1" 1
        return -1