class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = defaultdict(int)
        n = len(s)
        res = 1 
        if n<1:
            return 0
        m[s[0]] = 1
        l = 0
        r = 0
        while r<n-1:
            r+=1
            m[s[r]] += 1 
            if m[s[r]]==1:
                res = max(res, r-l+1)
            else:
                while s[l] != s[r]:
                    m[s[l]] -= 1 
                    l+=1
                m[s[l]] -= 1 
                l+=1 #step pass that dupe
        return res





        # try stepping to right, if okay then check len and next 
        # if not okay then shrink from left until a char has 2 count