class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = ""
        smoll = 0
        n = len(strs)
        n1 = len(strs[0])
        if n > 1:
            n2 = len(strs[1])
            if n1 <= n2:
                smoll = n1
            else: smoll = n2
        else: smoll = n1
        if n > 1:
            for s in range(smoll):
                if strs[0][s] == strs[1][s]:
                    a += strs[0][s]
                else:
                    break
            for i in range (1,n):
                for j in range(len(a)+1):
                    if a[:j] != strs[i][:j]:
                        a = a[:j-1]
                        print(a)
            return a
        else: return strs[0]