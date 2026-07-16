class Solution:
    def isLeft(self, c: str) -> bool:
        if c == '(' or c=='{' or c=='[':
            return True 
        return False

    def isValid(self, s: str) -> bool:
        m = { ')':'(', '}':'{', ']':'[' }
        stack = []
        for c in s: 
            if self.isLeft(c):
                stack.append(c)
            else:
                if not stack:
                    return False
                temp = stack.pop()
                if m[c] != temp:
                    return False 
        return not stack