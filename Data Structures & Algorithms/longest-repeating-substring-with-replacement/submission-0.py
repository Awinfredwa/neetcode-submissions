class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        n = len(s)
        if n<= 1:
            return 1; 
        l = 0
        count[s[0]] = 1
        maxf = 1
        res = 1
        for r in range(1, n):
            count[s[r]]+=1
            maxf = max(maxf, count[s[r]])
            if r - l + 1 - maxf <= k:
                res = max(res, r-l+1)
            else:
                count[s[l]]-=1
                l+=1
            
        return res 




