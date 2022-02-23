class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if not stack:
                    return False
                elif ch == ')' and stack[-1] != '(':
                    return False
                elif ch == '}' and stack[-1] != '{':
                    return False
                elif ch == ']' and stack[-1] != '[':
                    return False
                stack.pop()
        if stack:
            return False
        else:
            return True
