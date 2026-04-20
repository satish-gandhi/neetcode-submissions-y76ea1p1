class Solution:
    def isValid(self, s: str) -> bool:
        cto = {
            ')': '(', '}': '{', ']': '['
        }

        stack = []
        for b in s:
            if b in cto:
                if stack and stack[-1]==cto[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return True if not stack else False 


