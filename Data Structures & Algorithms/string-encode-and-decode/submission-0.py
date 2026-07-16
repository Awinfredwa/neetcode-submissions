class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + "a" + s
        return res 

# 3abbb4a
    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0 
        res = []

        while i < n:
            l = ""
            while s[i].isdigit():
                l+=s[i]
                i += 1
            # skip that 'a'
            i += 1
            curr = ""
            for j in range(0, int(l)):
                curr += s[i]
                i += 1 
            res.append(curr)
        return res
            
    

