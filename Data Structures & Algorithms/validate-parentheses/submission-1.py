class Solution:
    def isValid(self, s: str) -> bool:
        opentoclose = {')': '(', ']': '[', '}': '{'}
        stack = []
        for p in s:
            if p in opentoclose.values():
                stack.append(p)
            elif stack and opentoclose[p]==stack[-1]:
                stack.pop(-1)
            else:
                return False
        if not stack:
            return True
        else:
            return False
